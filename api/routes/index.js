var express = require('express');
var router = express.Router();

let actions = [];

router.post('/actions', function (req, res, next) {
    actions.push(req.body.action);
    res.send().ok;
});

router.get('/actions', function (req, res, next) {
    res.send(actions);
    actions = actions.slice(1, actions.length);
});

module.exports = router;
