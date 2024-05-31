const express = require('express');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());

// Read messages from JSON file
const messages = JSON.parse(fs.readFileSync('messages.json', 'utf8'));

// Endpoint to get a random message
app.get('/random-message', (req, res) => {
    const randomIndex = Math.floor(Math.random() * messages.length);
    const randomMessage = messages[randomIndex];
    console.log(randomMessage.sender)
    console.log(randomMessage.message)
    res.json(randomMessage);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
