quest_project for managing player quests

## Setup

How to start and run the app, from a fresh clone:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run_dev.py
flask run
```

## Environment variables

Create a '.env' file in the project root with values like:

```env
JWT_SECRET_KEY=change-me-in-dev
INTERNAL_SERVICE_TOKEN=dev-internal-token
DATABASE_URL=sqlite:///dev.db
FLASK_DEBUG=1
FLASK_TESTING=0
```

## Database and migrations

by default, the app uses a local SQLite database at `instance/dev.db` when `DATABASE_URL` is not set.

A migration workflow with Flask-Migrate is installed but not initialized yet (no `migrations/` folder). You can work against the default SQLite dev database for now.