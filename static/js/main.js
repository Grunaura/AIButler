/*
Author: Adam Messick
Date: 5/24/2023
This file contains all custom JavaScript for the webpages.
*/

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Collect form data
        let formData = new FormData(form);

        // Prepare data to be sent to the server
        let data = {};
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }

        // Send data to the server
        fetch('/result', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            document.getElementById('results').innerHTML = JSON.stringify(data, null, 2);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
