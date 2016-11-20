var webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

var path = require('path');
var _root = path.resolve(__dirname, '..');

function root(args) {
  args = Array.prototype.slice.call(arguments, 0);
  return path.join.apply(path, [_root].concat(args));
}


module.exports = {
    devtool: 'eval',

    entry: {
        'polyfills': './src/polyfills.ts',
        'vendor': './src/vendors.ts',
        'main': './src/main.ts'
    },

    output: {
        path: root('./static/'),
        publicPath: '/static',
        filename: '[name].js',
        chunkFilename: '[id].chunk.js'
    },

    resolve: {
        extensions: [".js", ".ts"]
    },

    module: {
        loaders: [
            { test: /\.js$/, loader: 'source-map-loader', exclude: [ root('node_modules/bootstrap') ] },
            { test: /\.ts$/, loaders: ['ts', 'angular2-template-loader'] },

            { test: /\.html$/, loader: "raw-loader", exclude: [root("src/index.html")] },
            { test: /\.css$/, loader: "raw-loader" },

            { test: /\.(png|jpe?g|gif|svg|woff|woff2|ttf|eot|ico)$/, loader: 'file?name=assets/[name].[hash].[ext]' }
        ]
    },

    plugins: [
        new webpack.ContextReplacementPlugin(/angular(\\|\/)core(\\|\/)(esm(\\|\/)src|src)(\\|\/)linker/, root("./src")),
        new webpack.ProgressPlugin(),

        new ExtractTextPlugin("style.css"),

        new webpack.optimize.CommonsChunkPlugin({
            name: ['app', 'vendor', 'polyfills']
        }),

        new HtmlWebpackPlugin({
            template: './src/index.html'
        })
    ]

};
