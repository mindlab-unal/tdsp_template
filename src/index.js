const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const fileUpload = require('express-fileupload');
const ExpressServer = require('./serverHandler/Express');
const utils = require('./utils');

const port = utils.server.getPortNumber();

const app = new ExpressServer(port);

const middlewares = [
    cors(),
    morgan('dev'),
    express.urlencoded({extended: false}),
    express.json(),
    fileUpload()
];

app.loadMiddlewares(middlewares)
.loadRoutes('api', '../api')
.all('*', (req, res) => {
    res.status(404).json({
        message: 'Not found'
    });
}).run();
