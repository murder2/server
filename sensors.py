#!/usr/bin/env python3

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.web

from models import IntegrityError


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class SensorsHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    def get(self, *args, **kwargs):
        self.finish(dict(actors=list(self.data.sensors.values())))

    def post(self, *args, **kwargs):
        body = tornado.escape.json_decode(self.request.body)

        try:
            self.data.addSensor(id=body["name"])
        except IntegrityError:
            self.set_status(409)
            self.finish(dict(name=body["name"], error="Name already existing"))
        else:
            self.set_status(201)
            self.finish()


class SensorDetailsHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    def get(self, sensor_id, *args, **kwargs):
        sensor = self.data.sensors.get(sensor_id)

        if sensor is None:
            self.set_status(404)
            self.finish()
            return

        self.finish(sensor)

    def put(self, sensor_id, *args, **kwargs):
        sensor = self.data.sensors.get(sensor_id)

        if sensor is None:
            self.set_status(404)
            self.finish()
            return

        # FIXME handle renaming
        print("Put on SensorDetailsHandler not yet handled")
        self.finish()
