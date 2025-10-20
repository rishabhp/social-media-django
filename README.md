# social-media-django

This is a Django-based web application.

## Getting Started

Follow these steps to set up the project locally.

### 1. Set Up Virtual Environment (Optional but Recommended)

    python -m venv venv
    source venv/bin/activate        # On Linux/macOS
    venv\Scripts\activate           # On Windows

### 2. Install Required Libraries

Make sure you're in the project root directory (where `requirements.txt` is located), then run:

    pip install -r requirements.txt

### 3. Run Database Migrations

Since database files are not committed to the repository, initialize the database by running:

    python manage.py migrate

### 4. Create a Superuser

Create an admin user to access Django’s admin panel:

    python manage.py createsuperuser

Follow the prompts to set up your username, email, and password.

### 5. Run the Development Server

Start the Django development server:

    python manage.py runserver

Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the app in action.

---

## Notes

- Make sure you are using a compatible Python version (e.g., Python 3.8+).
- The `.env` or any secret config files are **not** committed for security.
- Access the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

---
