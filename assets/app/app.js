var angular = require("angular");

angular
    .module("app.notes", [
        "ui.router"
    ])
    .config([
        "$locationProvider",
        "$stateProvider",
        config
    ]);

function config($locationProvider, $stateProvider) {

    $locationProvider.html5Mode(true);

    $stateProvider
        .state("list", {
            url: "/",
            templateUrl: "tpl/list.html",
            controller: "NoteIndexCtrl as vm"
        })

        .state("new", {
            url: "/new/",
            templateUrl: "tpl/new.html",
            controller: "NoteFormCtrl as vm"
        })

        .state("details", {
            url: "/details/:id/",
            templateUrl: "tpl/details.html",
            controller: "NoteDetailsCtrl as vm"
        });
}
