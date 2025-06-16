# Stakels

This repository contains a minimal base for an application that allows friends to place bets with each other.

The project uses a simple Flask server and an in-memory store for users and bets. It's intended as a starting point for further development.

## Setup

1. Ensure you have Python 3.9+ installed and then install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the development server:

```bash
python -m stakels.server
```

This will start a local web server on `http://127.0.0.1:5000` with the following endpoints:

- `POST /users` – create a user, JSON body `{"username": "name"}`.
- `POST /bets` – create a bet, JSON body `{"description": "...", "amount": 10, "creator": "alice", "opponent": "bob"}`.
- `GET /bets` – list all created bets.

After launching the server you can visit `http://127.0.0.1:5000/` to access a small
testing UI for manually creating users and bets.

## Running Tests

Tests are provided with `pytest`:

```bash
pytest
```
