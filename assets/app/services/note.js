var angular = require("angular");

angular
    .module("app.notes")
    .service("Note", [
        "$resource",
        Note
    ]);


function Note($resource) {
    return $resource("/api/notes/:id/");
}
