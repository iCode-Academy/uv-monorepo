# Django Monorepo

This is a monorepo for Django projects.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -e ".[dev]"`
5. Install pre-commit hooks: `pre-commit install`
6. Run migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Development

### Adding a new app

To add a new app to the monorepo:

```bash
python manage.py startapp app_name src/apps/app_name
```
