const { Router } = require("express");

const router = Router();
const ImagesController = require("../controllers/Images.Controller");

const imageController = new ImagesController();

router.post("/", imageController.catchImages);  

module.exports = router;