#!/usr/bin/env python3

from collections import defaultdict

__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class IntegrityError(Exception):
    def __init__(self, id):
        self.id = id


class Data:
    actor_id = 0
    beacon_id = 0

    actors = dict()  # containing capabilities, ip, port, id, actions
    sensors = dict()
    links = defaultdict(lambda: defaultdict(dict))

    def addActor(self, ip, port, capabilities):
        self.actors[str(self.actor_id)] = dict(capabilities=capabilities, ip=str(ip), port=port, id=str(self.actor_id), actions=[])
        self.actor_id += 1

        return self.actor_id - 1

    def addSensor(self, id):
        if id in self.sensors.keys():
            raise IntegrityError(id)

        self.sensors[str(id)] = dict(id=str(id), beacons=[])
