const webpack = require("webpack");
const path = require("path");

const config = {

    devtool: "source-map",

    entry: {
        app: [
            "./assets/app/app.js",
        ],

        lib: [
            "angular",
            "lodash",
        ]
    },

    output: {
        path: path.resolve(__dirname, "assets/dist/"),
        filename: "[name].bundle.js"
    },

    plugins: [
        new webpack.optimize.UglifyJsPlugin({
            compress: {warnings: false},
            output: {comments: false},
            sourceMap: true
        }),
        new webpack.optimize.CommonsChunkPlugin({
            names: "lib"
        })
    ]
};

module.exports = config;
