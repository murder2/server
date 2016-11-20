import { Component, ViewEncapsulation } from "@angular/core";
import {MurderService} from "./murder.service";
import {Sensor, Actor} from "./stub";
import {Response} from "@angular/http";


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
    public eventModal: boolean;
    public actionModal: boolean;

    public newAction: any;
    public newEvent: any;

    public event: Sensor = null;
    public event_uid: string = null;
    public event_major: number = null;
    public event_minor: number = null;

    public actor: Actor = null;
    public action_type: string = null;
    public sound_file: string = null;
    public action_name: string = null;

    constructor(public service: MurderService) {}

    setAction(o: any) {
        this.newAction = o;
    }

    setEvent(o: any) {
        this.newEvent = o;
    }

    addEvent() {
        this.eventModal = true;
    }

    addAction() {
        this.actionModal = true;
    }

    submitEvent() {
        this.service.addEvent(this.event, this.event_uid, this.event_major, this.event_minor).subscribe((e: Response) => {
            this.event_uid = null;
            this.event_major = null;
            this.event_minor = null;
            this.eventModal = false;
        });
    }

    submitAction() {
        this.service.addAction(this.actor, this.action_name, this.action_type, this.sound_file).subscribe(() => {
            this.actor = null;
            this.action_type = null;
            this.sound_file = null;
            this.actionModal = false;
        })
    }
}
