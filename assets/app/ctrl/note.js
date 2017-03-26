var angular = require("angular");

angular
    .module("app.notes")
    .controller("NoteIndexCtrl", [
        "Note",
        NoteIndexCtrl
    ])
    .controller("NoteFormCtrl", [
        "Note",
        "note",
        NoteFormCtrl
    ])
    .controller("NoteDetailsCtrl", [
        "note",
        NoteDetailsCtrl
    ]);


function NoteIndexCtrl(Note) {

    var vm = this;

    vm.items = [];

    Note.get(function(data) {
        vm.items = data.items;
    });
}

function NoteFormCtrl(Note, note) {

    var vm = this;

    vm.note = note || new Note();
}


function NoteDetailsCtrl(note) {

    var vm = this;

    vm.note = note;
}
