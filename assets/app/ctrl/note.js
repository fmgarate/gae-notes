var angular = require("angular");

angular
    .module("app.notes")
    .controller("NoteIndexCtrl", [
        NoteIndexCtrl
    ])
    .controller("NoteFormCtrl", [
        NoteFormCtrl
    ])
    .controller("NoteDetailsCtrl", [
        NoteDetailsCtrl
    ]);


function NoteIndexCtrl() {
    console.log("NoteIndexCtrl");
}

function NoteFormCtrl() {
    console.log("NoteFormCtrl");
}

function NoteDetailsCtrl() {
    console.log("NoteDetailsCtrl");
}
