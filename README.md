# KanMind Forum Backend

Simple Django REST API for a mini forum with user registration, authentication, posts, and comments.

---

## Setup / Quick Start

Run the following commands to set up and start the project locally:

```bash
# Clone repository
git clone <your-repository-url>
cd project_forum/backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (Linux / Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

---

## Table of Contents

- Project Overview
- Tech Stack
- Project Structure
- API Overview
- Authentication
- Development Notes

---

## Project Overview

This project provides a backend API for a simple forum application.
Users can register, log in, create posts, and write comments.
Authentication is handled via token-based authentication using Django REST Framework.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Token Authentication

---

## Project Structure

```bash
backend/
│
├── core/                  # Django project settings
├── user_auth_app/         # Authentication (register, login)
│   └── api/
├── forum_app/             # Posts and comments
│   └── api/
├── manage.py
└── requirements.txt
```

---

## API Overview

### Auth Endpoints

- `POST /auth/register/`
- `POST /auth/login/`

### Forum Endpoints

- `GET /api/posts/`

- `POST /api/posts/`

- `GET /api/posts/<id>/`

- `PUT /api/posts/<id>/`

- `DELETE /api/posts/<id>/`

- `GET /api/comments/`

- `POST /api/comments/`

- `GET /api/comments/<id>/`

- `PUT /api/comments/<id>/`

- `DELETE /api/comments/<id>/`

---

## Authentication

Authentication is handled via token authentication.

After login, a token must be included in the request header:

Authorization: Token "your-token"

---

## Development Notes

- Default permission: authenticated users only
- Custom permissions will restrict update/delete actions to object owners
- Admin interface is available at `/admin/`
- API development is done step-by-step with immediate Postman testing
