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
    constructor(public service: MurderService) {
        service.fetch();
    }
}
