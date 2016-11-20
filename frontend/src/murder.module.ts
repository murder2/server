import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import {MurderComponent} from "./murder.component";
import {MurderService} from "./murder.service";


@NgModule({
    bootstrap: [MurderComponent],
    declarations: [MurderComponent],
    imports: [
        BrowserModule,
    ],
    providers: [MurderService],
})
export class MurderModule {}
