import { Component, EventEmitter, Output, HostBinding, ChangeDetectionStrategy } from "@angular/core";


/**
 * Modal component
 */
@Component({
    changeDetection: ChangeDetectionStrategy.OnPush,
    selector: "modal",
    styleUrls: ["./modal.css"],
    templateUrl: "./modal.html",
})
export class Modal {
    /**
     * Event emitted when the modal is opened
     */
    @Output() public onClose: EventEmitter<boolean> = new EventEmitter<boolean>();

    @HostBinding("class") public classes = "modal in";

}
