import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {MurderComponent} from "./murder.component";
import {MurderService} from "./murder.service";
import {HttpModule} from "@angular/http";
import {CommonModule} from "@angular/common";
import {Modal} from "./modal/modal.component";
import {FormsModule} from "@angular/forms";


@NgModule({
    bootstrap: [MurderComponent],
    declarations: [MurderComponent, Modal],
    imports: [
        BrowserModule,
        CommonModule,
        FormsModule,
        HttpModule,
    ],
    providers: [MurderService],
})
export class MurderModule {
}
