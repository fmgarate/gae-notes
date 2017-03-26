var angular = require("angular");

angular
    .module("app.notes", [
        "ngResource",
        "ui.router"
    ])
    .config([
        "$locationProvider",
        "$resourceProvider",
        "$stateProvider",
        config
    ]);

function config($locationProvider, $resourceProvider, $stateProvider) {

    $locationProvider.html5Mode(true);
    $resourceProvider.defaults.stripTrailingSlashes = false;

    $stateProvider
        .state("list", {
            url: "/",
            templateUrl: "tpl/list.html",
            controller: "NoteIndexCtrl as vm"
        })

        .state("new", {
            url: "/new/",
            templateUrl: "tpl/new.html",
            controller: "NoteFormCtrl as vm",
            resolve: {
                note: [function() {
                    return null;
                }]
            }
        })

        .state("note", {
            url: "/note/{id}/",
            templateUrl: "tpl/note.html",
            controller: "NoteDetailsCtrl as vm",
            resolve: {
                note: ["$stateParams", "Note", function($stateParams, Note) {
                    return Note.get({id: $stateParams.id}).$promise;
                }]
            }
        });
}
