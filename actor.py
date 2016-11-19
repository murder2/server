#!/usr/bin/env python3
import json

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.web


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class ActorsHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    def get(self, *args, **kwargs):
        self.finish(dict(actors=list(self.data.actors.values())))

    def post(self, *args, **kwargs):
        body = tornado.escape.json_decode(self.request.body)

        self.data.addActor(
            ip=self.request.headers.get("X-Real-IP") or self.request.remote_ip,
            port=body["port"],
            capabilities=body["capabilities"]
        )

        self.finish()


class ActorDetailsHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    def put(self, actor_id, *args, **kwargs):
        actor = self.data.actors.get(actor_id)

        if actor is None:
            self.set_status(404)
            self.finish()
            return

        # FIXME handle renaming
        print("Put on ActorDetailsHandler not yet handled")
        self.finish()


class ActorActionsHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    @tornado.gen.coroutine
    def put(self, actor_id, *args, **kwargs):
        actor = self.data.actors.get(actor_id)

        if actor is None:
            self.set_status(404)
            self.finish()
            return

        actor["actions"].append(tornado.escape.json_decode(self.request.body))

        http = tornado.httpclient.AsyncHTTPClient()
        yield http.fetch("http://{ip}:{port}/actions/{id}".format(
            ip=actor["ip"], port=actor["port"], id=len(actor["actions"])
        ), body=self.request.body, method="PUT")

        self.finish()
