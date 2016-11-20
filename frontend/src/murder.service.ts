import { ReplaySubject } from "rxjs/Rx";
import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import {Action, Actor, Sensor} from "./stub";


@Injectable()
export class MurderService {
    public actions$ = new ReplaySubject<Action[]>(1);
    public actors$ = new ReplaySubject<Actor[]>(1);
    public events$ = new ReplaySubject<Event[]>(1);
    public sensors$ = new ReplaySubject<Sensor[]>(1);
    public links$ = new ReplaySubject<any[]>(1);

    constructor(public http: Http) {
        this.fetchActions();
    }

    public fetchActions() {
        this.http.get("/actors").subscribe((res: Response) => {
            console.log(res);
        })
    }


    public addEvent(sensor: Sensor, beacon_uid: string, beacon_minor: string, beacon_major: string) {
        return this.http.put(`/sensors/${sensor.id}`, {uid: beacon_uid, minor: beacon_minor, major: beacon_major})
    }
}
