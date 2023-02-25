const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Use bodyParser to parse JSON request bodies
app.use(bodyParser.json());

// Route to handle form submission
app.post('/', (req, res) => {
  const { query } = req.body;

  // Log the query to the console
  console.log(`Received query: ${query}`);

  // Send a simple response back to the frontend
  res.json({ response: 'Hello world!' });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
