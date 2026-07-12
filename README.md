# Photo Gallery

A simple Photo Gallery web app built with Django for a school assignment.
Users can register, log in, browse photos, view photo details, filter
photos by tag, like/dislike photos, and manage their profile.

**Live demo:** TODO - add your Render URL here after deploying, e.g.
`https://your-app-name.onrender.com`

## Tech stack

- Python 3 + Django 3.2
- PostgreSQL (database)
- HTML5 + Tailwind CSS (loaded from the Tailwind CDN, the simplest way
  to use Tailwind in a beginner project)
- Pillow (so Django can handle uploaded images)

## Features

- Register, log in, log out, and change password (Django's built-in auth)
- A profile page where you can add a bio and profile picture
- A homepage that shows every photo in the gallery
- A detail page for each photo, showing its title, description, and tags
- Filtering photos by tag
- Liking and disliking photos

Photos and tags are added through the Django admin site at `/admin/`
(there is no separate "upload" page in this beginner version).

## Running the project locally

### 1. Clone the project and set up a virtual environment

```bash
git clone https://github.com/emmanuelopeto7-star/Django_photo_gallary.git
cd Django_photo_gallary
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Create a PostgreSQL database

Install PostgreSQL if you don't already have it, then create a database
and user for this project. For example, using `psql`:

```sql
CREATE DATABASE photogallery_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE photogallery_db TO postgres;
```

`photogallery/settings.py` reads the database name, user, password,
host, and port from environment variables, with these defaults:

| Setting  | Environment variable | Default          |
|----------|-----------------------|-------------------|
| Name     | `DB_NAME`             | `photogallery_db` |
| User     | `DB_USER`             | `postgres`        |
| Password | `DB_PASSWORD`         | `postgres`        |
| Host     | `DB_HOST`             | `localhost`       |
| Port     | `DB_PORT`             | `5432`            |

If your local PostgreSQL uses different values, either set the
environment variables to match, or edit the defaults directly in
`photogallery/settings.py`. Never commit your real password to git.

### 3. Run migrations and create an admin user

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and
`http://127.0.0.1:8000/admin/` to log in as the superuser and add tags
and photos.

## Deploying to Render

1. Push this project to GitHub (already done if you're reading this
   from the repo).
2. Create a free account at [render.com](https://render.com).
3. In the Render dashboard, click **New +** and add a **PostgreSQL**
   database. Copy the connection details it gives you (name, user,
   password, host, port).
4. Click **New +** again and choose **Web Service**, then connect your
   GitHub repository.
5. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python manage.py migrate && gunicorn photogallery.wsgi`
     (add `gunicorn` to `requirements.txt` first, since Render needs a
     production web server instead of `runserver`)
6. Add environment variables in the Render dashboard matching the
   PostgreSQL database from step 3: `DB_NAME`, `DB_USER`,
   `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
7. Also add `DJANGO_SECRET_KEY` (any random string) and update
   `photogallery/settings.py` to read `SECRET_KEY` and `ALLOWED_HOSTS`
   from environment variables before deploying, so your real secret
   key isn't in git and Render's domain is allowed.
8. Click **Create Web Service**. Render will build and deploy the app.
9. Once it's live, copy the URL Render gives you and paste it at the
   top of this README in place of the TODO.

## Project structure

```
Django_photo_gallary/
├── gallery/            # The app: models, views, forms, admin, urls
├── photogallery/        # Project settings and root urls
├── templates/           # HTML templates (base, gallery, registration)
├── requirements.txt      # Python dependencies
└── manage.py
```
