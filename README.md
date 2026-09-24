# Farm Plant Explorer

A small Kivy desktop learning project that looks up plant information through the OpenFarm API. The entry-point filename is `chatbot.py`, but the application is a plant lookup interface.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python chatbot.py
```

The application validates empty input and handles network, HTTP, and invalid-response failures without crashing.

## Project scope

This project demonstrates Python API integration and a Kivy user interface.

## License

MIT
