var express = require('express');
var router = express.Router();

let actions = [];

router.post('/actions', function (req, res, next) {
    if(Array.isArray(req.body.action)){
        actions = [...actions, ...req.body.action]
    } else {
        actions.push(req.body.action);
    }

    res.send().ok;
});

router.get('/actions', function (req, res, next) {
    res.send(actions);
    actions = [];
});

module.exports = router;
