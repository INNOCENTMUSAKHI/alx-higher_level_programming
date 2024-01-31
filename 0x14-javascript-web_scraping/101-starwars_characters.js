#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
if (!id) {
    console.error('Usage: ./script.js <film_id>');
    process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error.message);
    } else {
        const content = JSON.parse(body);
        const characters = content.characters;

        for (const characterUrl of characters) {
            request.get(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error.message);
                } else {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                }
            });
        }
    }
});

