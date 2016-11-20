import { Component, ViewEncapsulation } from "@angular/core";
import {MurderService} from "./murder.service";


/**
 * Main component for the application
 */
@Component({
    encapsulation: ViewEncapsulation.None,
    selector: "murder",
    styleUrls: ["./murder.css"],
    templateUrl: "./murder.html",
})
export class MurderComponent {
    public newAction: any;
    public newEvent: any;

    constructor(public service: MurderService) {
        service.fetch();
    }

    setAction(o: any) {
        this.newAction = o;
    }

    setEvent(o: any) {
        this.newEvent = o;
    }
}
