import { platformBrowser } from "@angular/platform-browser";
import { enableProdMode } from "@angular/core";
import { MurderModuleNgFactory } from "../compiled/src/murder.module.ngfactory";


if (process.env.ENV === "production") {
    // Production
    enableProdMode();
}

/**
 * Bootstraps the application
 */
platformBrowser().bootstrapModuleFactory(MurderModuleNgFactory).then(() => {
    let loading = document.getElementById("loading-screen");

    function cleanup() {
        document.styleSheets[0].disabled = true;
        loading.remove();
    }

    loading.addEventListener("webkitTransitionEnd", cleanup, false);
    loading.addEventListener("oTransitionEnd", cleanup, false);
    loading.addEventListener("transitionend", cleanup, false);
    loading.addEventListener("msTransitionEnd", cleanup, false);

    loading.classList.add("hidden");
});
