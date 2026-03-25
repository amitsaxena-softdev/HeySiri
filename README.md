# HeySiri (Production-Ready Architecture + UI)

This project is now structured as a production-ready Python web application with:

- **Flask app factory architecture**
- **Dedicated API layer** (`/api/chat`, `/api/health`)
- **Service layer for LLM integrations**
- **Command processing core with clear business logic boundaries**
- **Simple responsive web UI**
- **Config via environment variables**
- **Unit tests for command behavior**

## Project Structure

```text
siri_assistant/
  api/
    routes.py
    schemas.py
  core/
    command_processor.py
  services/
    llm_service.py
  web/
    templates/index.html
    static/styles.css
    static/app.js
  app.py
  config.py
  logging_config.py
main.py
tests/
requirements.txt
```

## Quickstart

1. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure environment:
   ```bash
   export OPENAI_API_KEY="your-key"
   export HEY_SIRI_OPENAI_MODEL="gpt-4o-mini"
   export HEY_SIRI_HOST="127.0.0.1"
   export HEY_SIRI_PORT="8000"
   ```

3. Run app:
   ```bash
   python main.py
   ```

4. Open `http://127.0.0.1:8000` in a browser.

## API

### POST `/api/chat`

Request:

```json
{ "query": "open youtube" }
```

Response:

```json
{ "text": "Opening youtube.", "action": "open_url", "url": "https://youtube.com" }
```

### GET `/api/health`

Response:

```json
{ "status": "ok" }
```
