# AI Coding Guidelines for myBackend Chatbot Server

## Project Overview
This is a Flask-based chatbot server using Flask-RESTX for API endpoints. It supports user management in chat rooms with PostgreSQL backend. Follows Test-Driven Development (TDD) with nose testing framework.

## Architecture
- **API Layer**: All endpoints defined in `API/endpoints.py` as Flask-RESTX Resource classes
- **Data Layer**: Database interactions in `db/db.py` (currently stubs, transitioning to PostgreSQL)
- **Testing**: Unit tests in `API/tests/test_endpoints.py` using unittest
- **Deployment**: Gunicorn via `Proc` file

Example endpoint structure:
```python
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'Hola': 'mundo'}
```

## Development Workflow
- **Environment**: Use `annavenv` virtual environment (`source annavenv/bin/activate`)
- **Install deps**: `pip3 install -r requirements/requirements-dev.txt`
- **Run tests**: `make unit` (nosetests with coverage on API package)
- **Lint**: `make lint` (flake8 on API/*.py and db/*.py)
- **Full test suite**: `make tests` (lint + unit)
- **Generate docs**: `make docs` (pydoc3 HTML in API/)
- **Deploy**: `make prod` (tests + git push)

## Conventions
- **Imports**: `import db.db as db` for database module
- **Docstrings**: Extensive docstrings on classes and methods for API documentation
- **Response format**: JSON objects, e.g., `{"Available endpoints": [...]}` in `/endpoints`
- **Error handling**: Use `HTTPStatus` from `http` module for responses
- **Database paths**: Hardcoded absolute paths like `ROOMS_DB = "/home/anna/website_project/myBackend/db/db/rooms.json"`
- **Testing**: Inherit from `TestCase`, test methods like `test_hello`

## Key Files
- `API/endpoints.py`: Main API endpoints
- `db/db.py`: Data store interactions (stubs to PostgreSQL)
- `makefile`: Build/test automation
- `requirements/`: Separate prod/dev/db requirements
- `Proc`: Gunicorn deployment config

## Patterns
- **Endpoint discovery**: `/endpoints` returns all available routes dynamically
- **User creation**: POST `/create_user/<username>&<password>&<email>` (note URL parameter format)
- **Data stubs**: Functions return fake data until real DB integration, e.g., `fetch_pets()` returns animal counts</content>
<parameter name="filePath">\\wsl.localhost\Ubuntu-22.04\home\anna\website_project\myBackend\.github\copilot-instructions.md