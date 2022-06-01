

class ImagesController {

    catchImages(req, res) { 
        const { file } = req;
        const { originalname, mimetype, size } = file;
        const image = {
            originalname,
            mimetype,
            size
        };
        res.json(image);
    }
}

module.exports = ImagesController;