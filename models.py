#!/usr/bin/env python3


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class IntegrityError(Exception):
    def __init__(self, id):
        self.id = id


class Data:
    actor_id = 0
    beacon_id = 0

    actors = dict()  # containing capabilities, ip, port, id, actions
    sensors = dict()
    links = dict()

    def addActor(self, ip, port, capabilities):
        self.actors[str(self.actor_id)] = dict(capabilities=capabilities, ip=str(ip), port=port, id=self.actor_id, actions=[])
        self.actor_id += 1

    def addSensor(self, id):
        if id in self.sensors.keys():
            raise IntegrityError(id)

        self.sensors[id] = dict(id=id, beacons=[])
