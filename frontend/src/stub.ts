export class Beacon {

    constructor(public major: number, public minor: number, public uid: string, public friendlyName: string = null) {}

}

export class Sensor {

    constructor(public id: string, public beacons: Beacon[], public friendlyName: string = null) {}

}

export class Action {

    constructor(public type: string, public name: string, public extras: string) {}

}

export class Actor {

    constructor(public id: string, public ip: string, public port: number, public capabilities: string[], public actions: Action[],  public friendlyName: string = null) {}

}

