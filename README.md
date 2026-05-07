# Forum Backend

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

- [KanMind Forum Backend](#kanmind-forum-backend)
  - [Setup / Quick Start](#setup--quick-start)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [API Overview](#api-overview)
    - [Auth Endpoints](#auth-endpoints)
    - [Post Endpoints](#post-endpoints)
    - [Comment Endpoints](#comment-endpoints)
  - [Authentication](#authentication)
  - [Permissions](#permissions)
    - [Global Rule](#global-rule)
    - [Object-Level Rule](#object-level-rule)
  - [Admin Interface](#admin-interface)
  - [Development Notes](#development-notes)

---

## Project Overview

This project provides a backend API for a simple forum application.
Users can register, log in, create posts, and write comments.
Authentication is handled via token-based authentication using Django REST Framework.

---

## Features

- User registration
- User login with token authentication
- Create and list posts
- Retrieve, update, and delete single posts
- Create and list comments
- Retrieve, update, and delete single comments
- Object-level permission control for posts and comments

---

## Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication
- SQLite3
- Postman for API testing

---

## Project Structure

```text
backend/
│
├── core/                  # Django project settings and root URL configuration
├── user_auth_app/         # Authentication logic
│   └── api/
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
├── forum_app/             # Forum logic for posts and comments
│   └── api/
│       ├── permissions.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
├── manage.py
└── requirements.txt
```

---

## API Overview

### Auth Endpoints

- `POST /auth/register/`
- `POST /auth/login/`

### Post Endpoints

- `GET /api/posts/`
- `POST /api/posts/`
- `GET /api/posts/<id>/`
- `PATCH /api/posts/<id>/`
- `DELETE /api/posts/<id>/`

### Comment Endpoints

- `GET /api/comments/`
- `POST /api/comments/`
- `GET /api/comments/<id>/`
- `PATCH /api/comments/<id>/`
- `DELETE /api/comments/<id>/`

---

## Authentication

Authentication is handled via token authentication.

After login, a token must be included in the request header:

```text
Authorization: Token <your-token>
```

---

## Permissions

The project uses authenticated access as the default permission rule.

### Global Rule

Only authenticated users can access forum endpoints.

### Object-Level Rule

Posts and comments use a custom object-level permission:

- the owner of an object may update or delete it
- a superuser may also update or delete foreign objects
- other authenticated users have read-only access on detail endpoints

---

## Admin Interface

The Django admin interface is available at:

```text
/admin/
```

Posts and comments are registered in the admin interface and can be managed there.

---

## Development Notes

- The default DRF permission is `IsAuthenticated`
- Login is implemented with DRF's built-in `obtain_auth_token` view
- Post and comment authors are assigned automatically from the authenticated request user
- `author` and `created_at` are read-only serializer fields
- API development and validation were tested step by step with Postman
