# HTTP Form Save-to-File Server

A minimal HTTP server built with raw Python sockets that accepts user input via a web form and saves the submitted data to a file.

---

## Features

- Accepts POST requests with form data
- Parses `name`, `age`, and `email` manually
- Saves data to a local `.txt` file (`data.txt`)
- Responds with a confirmation message to the browser

---

## How It Works

1. User fills out a form in the browser.
2. The browser sends a POST request with body like:
