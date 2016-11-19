#!/usr/bin/env python3

import logging
import tornado.ioloop
import tornado.options
import tornado.web

from actor import ActorsHandler, ActorDetailsHandler, ActorActionsHandler
from models import Data
from sensors import SensorDetailsHandler, SensorsHandler


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


tornado.options.define("port", default=8000, type=int)

logger = logging.getLogger("tornado.application")


data = Data()


def make_app():
    return tornado.web.Application([
        (r"^/actors$", ActorsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)$", ActorDetailsHandler, dict(data=data)),
        (r"^/actors/([0-9]+)/actions$", ActorActionsHandler, dict(data=data)),
        (r"^/sensors$", SensorsHandler, dict(data=data)),
        (r"^/sensors/([a-zA-Z0-9])$", SensorDetailsHandler, dict(data=data))
    ])


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)
    logger.info("Running on port {}".format(tornado.options.options.port))

    tornado.ioloop.IOLoop.current().start()
