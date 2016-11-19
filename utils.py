#!/usr/bin/env python3


import logging

import tornado.escape
import tornado.gen
import tornado.httpclient
import tornado.web


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


logger = logging.getLogger("tornado.application")


class BaseHandler(tornado.web.RequestHandler):
    data = None

    def initialize(self, *args, **kwargs):
        self.data = kwargs["data"]

    def getOr404(self, collection, entry):
        data = collection.get(entry)

        if data is None:
            raise tornado.web.HTTPError(404)

        return data
