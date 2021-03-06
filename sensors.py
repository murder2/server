#!/usr/bin/env python3
import logging

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.web

from models import IntegrityError
from utils import BaseHandler


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


logger = logging.getLogger("tornado.application")


class SensorsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.finish(dict(sensors=list(self.data.sensors.values())))

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


class SensorDetailsHandler(BaseHandler):
    def get(self, sensor_id, *args, **kwargs):
        self.finish(self.getOr404(self.data.sensors, sensor_id))

    def put(self, sensor_id, *args, **kwargs):
        sensor = self.getOr404(self.data.sensors, sensor_id)
        body = tornado.escape.json_decode(self.request.body)

        sensor["beacons"] = body.get("beacons", [])

        # FIXME handle renaming
        logger.warn("Put on SensorDetailsHandler not yet handled")
        self.finish()


class EventHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self, sensor_id, *args, **kwargs):
        self.getOr404(self.data.sensors, sensor_id)

        body = tornado.escape.json_decode(self.request.body)

        major = body["major"]
        minor = body["minor"]

        # FIXME : handle sending event
        logger.debug("Sending event from {major}/{minor}".format(major=major, minor=minor))

        http = tornado.httpclient.AsyncHTTPClient()

        event = self.data.links[major][minor]

        print(event["actor"]["ip"], event["actor"]["port"])
        yield [
            http.fetch("http://{ip}:{port}/actions/{id}".format(
                id=action["id"],
                ip=event["actor"]["ip"],
                port=event["actor"]["port"]
            ))
            for action in self.data.links[major][minor]["actor"]["actions"]
        ]

        self.finish()


class BeaconHandler(BaseHandler):
    def get(self, *args, **kwargs):
        data = []
        for sensor in self.data.sensors.values():
            data.extend(sensor["beacons"])
        self.finish({"beacons": data})
