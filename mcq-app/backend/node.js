const express = require('express');
const app = express();
const bodyParser = require('body-parser');
let MCQ = ["prompt of the MCQ","choice 1","choice 2","choice 3","choice 4","1"]
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());
app.use(express.static('public'));
const cors = require('cors');

app.use(cors());
app.get('/', (req, res) => {
  res.send({
      MCQ
  });
});
app.post('/', (req, res) => {
  const data = req.body;
  console.log(data);
});
app.listen(3001, () => {
  console.log('Server listening on port 3001');
});