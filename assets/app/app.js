var angular = require("angular");

angular
    .module("app.notes", [
    ])
    .run([
        "$http",
        run
    ])


function run($http) {
    console.log("notes app ready");
}
