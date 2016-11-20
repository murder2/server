#!/usr/bin/env python3

import logging
import os

import tornado.ioloop
import tornado.options
import tornado.web

from actor import ActorsHandler, ActorDetailsHandler, ActorActionsHandler, ActionsHandler
from link import LinkHandler, LinkDetailsHandler
from models import Data
from sensors import SensorDetailsHandler, SensorsHandler, EventHandler, BeaconHandler


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


tornado.options.define("port", default=8000, type=int)
tornado.options.define("debug", default=False, type=bool)

logger = logging.getLogger("tornado.application")


data = Data()
static = os.path.join(os.path.dirname(__file__), "static")


class MainHandler(tornado.web.RequestHandler):
    debug = None

    def initialize(self, debug):
        self.debug = debug

    def get(self):
        self.render("index.html", debug=self.debug)


def make_app():
    settings = dict(
        static_path=static,
        autoreload=True,
        debug=tornado.options.options.debug
    )

    return tornado.web.Application([
        (r"^()/$", tornado.web.StaticFileHandler, dict(default_filename="index.html", path=static)),
        (r"^/actors$", ActorsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)$", ActorDetailsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)/actions$", ActorActionsHandler, dict(data=data)),
        (r"^/sensors$", SensorsHandler, dict(data=data)),
        (r"^/sensors/([a-zA-Z0-9]+)$", SensorDetailsHandler, dict(data=data)),
        (r"^/sensors/([a-zA-Z0-9]+)/event$", EventHandler, dict(data=data)),
        (r"^/beacons$", BeaconHandler, dict(data=data)),
        (r"^/actions$", ActionsHandler, dict(data=data)),
        (r"^/link$", LinkHandler, dict(data=data)),
        (r"^/link/([0-9]+)$", LinkDetailsHandler, dict(data=data)),
    ], **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)
    logger.info("Running on port {}".format(tornado.options.options.port))

    tornado.ioloop.IOLoop.current().start()
