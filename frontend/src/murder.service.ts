import { ReplaySubject } from "rxjs/Rx";
import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Action, Actor, Sensor, Beacon} from "./stub";


@Injectable()
export class MurderService {
    public actions$ = new ReplaySubject<Action[]>(1);
    public actors$ = new ReplaySubject<Actor[]>(1);
    public events$ = new ReplaySubject<Beacon[]>(1);
    public sensors$ = new ReplaySubject<Sensor[]>(1);
    public links$ = new ReplaySubject<any[]>(1);

    constructor(public http: Http) {
        this.fetchActors();
        this.fetchSensors();
        this.fetchEvents();
        this.fetchActions();
    }

    public fetchSensors() {
        this.http.get("/sensors").subscribe((res: Response) => {
            this.sensors$.next(res.json().sensors);
        })
    }

    public fetchEvents() {{
        this.http.get("/beacons").subscribe((res: Response) => {
            this.events$.next(res.json().beacons);
        })
    }}

    public fetchActors() {
        this.http.get("/actors").subscribe((res: Response) => {
            this.actors$.next(res.json().actors);
        })
    }

    public fetchActions() {
        this.http.get("/actions").subscribe((res: Response) => {
            this.actions$.next(res.json().actions);
        })

    }

    public addEvent(sensor: Sensor, beacon_uid: string, beacon_major: number, beacon_minor: number) {
        sensor.beacons.push(new Beacon(beacon_major, beacon_minor, beacon_uid));
        return this.http.put(`/sensors/${sensor.id}`, sensor).map((e: Response) => {
            this.fetchEvents();
            return e;
        });
    }

    public addAction(actor: Actor, action_name: string, action_type: string, sound_file: string) {
        return this.http.put(`/actors/${actor.id}/actions`, { name: action_name, type: action_type, sound_file: sound_file}).map((e: Response) => {
            this.fetchActions();
            return e;
        })
    }

    public addLink(a: Action, e: Beacon) {
        return this.http.post(`/link`, {event: e, action: a});
    }
}
