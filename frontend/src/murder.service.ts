import { ReplaySubject } from "rxjs/Rx";
import {Injectable} from "@angular/core";


@Injectable()
export class MurderService {
    public actions$ = new ReplaySubject<any[]>(1);

    public fetch() {
        this.actions$.next([{"title": "hello"}])
    }
}
