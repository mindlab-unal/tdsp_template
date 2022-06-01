const express = require('express');
const pluralize = require('pluralize');
const fs = require('fs');
const path = require('path');

const ExpressServer = class {
    constructor(port) {
        this.server = express();
        this.port = port;
    }

    loadRoutes(basePath, dirPath) {
        const API_PATH = path.join(__dirname, dirPath);

        fs.readdirSync(API_PATH).forEach((api) => {
            const plural = pluralize(api.replace('.ts', '').replace('.js', ''));

            if (plural.indexOf('.') === -1 && plural !== '__tests__') {
                this.server.use(`/${basePath}/${plural}`, require(`${API_PATH}/${api}`));
            }
        });

        return this;
    }

    all(path, callback) {
        this.server.all(path, callback);
        return this;
    }

    loadMiddlewares(middlewares) {
        middlewares.map(middleware => this.server.use(middleware));

        return this;
    }

    run() {
        this.server.listen(this.port, () => {
            console.log(`Server app listening on port ${this.port}!`);
        });
    }
}

module.exports = ExpressServer;