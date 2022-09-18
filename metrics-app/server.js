// metrics endpoint to query all my websites

const express = require('express');

const cors = require('cors');

const app = express();

app.use(cors({
  origin: true,
}));

app.use(express.json());

app.get('/', (request, response) => {
  response.status(200).send({ 'Instruction': 'Use (/metrics) endpoint to get all site metrics' });
});

app.get('/metrics', (request, response) => {
  response.status(200).send({ 'status': ' OK' });
});

app.listen(5000, (() => console.log('App listening on port 5000')));
