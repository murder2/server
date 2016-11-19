from tornado.httpclient import HTTPError

from utils import BaseHandler
import tornado.escape


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class LinkHandler(BaseHandler):
    def post(self, *args, **kwargs):
        body = tornado.escape.json_decode(self.request.body)

        event = body.get("event")
        if event is None:
            raise HTTPError(400, response=dict(error="Missing event"))

        event_major = event.get("major")
        event_minor = event.get("minor")

        if event_major is None:
            raise HTTPError(400, response=dict(error="Missing major on event field"))

        if event_minor is None:
            raise HTTPError(400, response=dict(error="Missing minor on event field"))

        action = body.get("action")
        if action is None:
            raise HTTPError(400, response=dict(error="Missing action field"))

        action_actor = action.get("actor")
        action_id = action.get("id")

        if action_actor is None:
            raise HTTPError(400, response=dict(error="Missing actor field on action"))

        if action_id is None:
            raise HTTPError(400, response=dict(error="Missing id on field action"))

        self.data.links[event_major][event_minor] = dict(actor=action_actor, id=action_id)

        self.finish()

        # FIXME check that major/minor already exists


class LinkDetailsHandler(BaseHandler):
    pass
