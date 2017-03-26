var angular = require("angular");

angular
    .module("app.notes")
    .controller("NoteIndexCtrl", [
        "Note",
        NoteIndexCtrl
    ])
    .controller("NoteFormCtrl", [
        "Note",
        NoteFormCtrl
    ])
    .controller("NoteDetailsCtrl", [
        "Note",
        "$state",
        NoteDetailsCtrl
    ]);


function NoteIndexCtrl(Note) {

    var vm = this;

    vm.items = [];

    Note.get(function(data) {
        vm.items = data.items;
    });
}

function NoteFormCtrl(Note) {
    console.log("NoteFormCtrl");
}

function NoteDetailsCtrl(Note, $state) {

    var vm = this;

    vm.note = {};

    Note.get({id: $state.params.id}, function(data) {
        vm.note = data;
    });
}
