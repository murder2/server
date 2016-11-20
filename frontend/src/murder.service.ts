import { ReplaySubject } from "rxjs/Rx";
import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Action, Actor, Sensor, Beacon} from "./stub";


@Injectable()
export class MurderService {
    public actions$ = new ReplaySubject<Action[]>(1);
    public actors$ = new ReplaySubject<Actor[]>(1);
    public events$ = new ReplaySubject<Event[]>(1);
    public sensors$ = new ReplaySubject<Sensor[]>(1);
    public links$ = new ReplaySubject<any[]>(1);

    constructor(public http: Http) {
        this.fetchActions();
        this.fetchSensors();
        this.fetchEvents();
    }

    public fetchSensors() {
        this.http.get("/sensors").subscribe((res: Response) => {
            this.sensors$.next(res.json().sensors);
        })
    }

    public fetchEvents() {{
        this.http.get("/beacons").subscribe((res: Response) => {
            console.log(res.json());
            this.events$.next(res.json().beacons);
        })
    }}

    public fetchActions() {
        this.http.get("/actors").subscribe((res: Response) => {
            console.log(res);
        })
    }


    public addEvent(sensor: Sensor, beacon_uid: string, beacon_major: number, beacon_minor: number) {
        sensor.beacons.push(new Beacon(beacon_major, beacon_minor, beacon_uid));
        return this.http.put(`/sensors/${sensor.id}`, sensor).map((e: Response) => {
            this.fetchEvents();
            return e;
        });
    }
}
