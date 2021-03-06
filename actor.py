#!/usr/bin/env python3
import logging

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.web

from utils import BaseHandler


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


logger = logging.getLogger("tornado.application")


class ActorsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.finish(dict(actors=list(self.data.actors.values())))

    def post(self, *args, **kwargs):
        body = tornado.escape.json_decode(self.request.body)

        uid = self.data.addActor(
            ip=self.request.headers.get("X-Real-IP") or self.request.remote_ip,
            port=body["port"],
            capabilities=body["capabilities"]
        )

        self.finish({'id': uid})


class ActorDetailsHandler(BaseHandler):
    def put(self, actor_id, *args, **kwargs):
        actor = self.getOr404(self.data.actors, actor_id)

        # FIXME handle renaming
        logger.warn("Put on ActorDetailsHandler not yet handled")
        self.finish()


class ActorActionsHandler(BaseHandler):
    @tornado.gen.coroutine
    def put(self, actor_id, *args, **kwargs):
        actor = self.getOr404(self.data.actors, actor_id)

        body = tornado.escape.json_decode(self.request.body)
        body["id"] = len(actor["actions"])
        actor["actions"].append(body)


        http = tornado.httpclient.AsyncHTTPClient()
        yield http.fetch("http://{ip}:{port}/actions/{id}".format(
            ip=actor["ip"], port=actor["port"], id=body["id"]
        ), body=self.request.body, method="PUT")

        self.finish()


class ActionsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        actions = []

        for actor in self.data.actors.values():
            actions.extend(actor["actions"])
        self.finish(dict(actions=actions))
