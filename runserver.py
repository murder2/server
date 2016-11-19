#!/usr/bin/env python3

import logging
import os

import tornado.ioloop
import tornado.options
import tornado.web

from actor import ActorsHandler, ActorDetailsHandler, ActorActionsHandler
from link import LinkHandler, LinkDetailsHandler
from models import Data
from sensors import SensorDetailsHandler, SensorsHandler, EventHandler


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


tornado.options.define("port", default=8000, type=int)

logger = logging.getLogger("tornado.application")


data = Data()

static = os.path.join(os.path.dirname(__file__), "static")


def make_app():
    settings = {
        "static_path": static,
        "cookie_secret": "THIS_SHOULD_NEVER_GET_PUSHED_TO_GITHUB",
        "xsrf_cookies": True,
        "autoreload": True,
    }

    return tornado.web.Application([
        (r"^()/$", tornado.web.StaticFileHandler, dict(default_filename="index.html", path=static)),
        (r"^/actors$", ActorsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)$", ActorDetailsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)/actions$", ActorActionsHandler, dict(data=data)),
        (r"^/sensors$", SensorsHandler, dict(data=data)),
        (r"^/sensors/([a-zA-Z0-9]+)$", SensorDetailsHandler, dict(data=data)),
        (r"^/sensors/([a-zA-Z0-9]+)/event$", EventHandler, dict(data=data)),
        (r"^/link/$", LinkHandler, dict(data=data)),
        (r"^/link/([0-9]+)$", LinkDetailsHandler, dict(data=data)),
    ], **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)
    logger.info("Running on port {}".format(tornado.options.options.port))

    tornado.ioloop.IOLoop.current().start()
