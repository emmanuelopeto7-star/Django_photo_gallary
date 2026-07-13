# Photo Gallery

A simple Django web app for browsing, uploading, tagging, and
liking/disliking photos. Built for a school assignment.

**Live demo:** TODO - add your Render URL here after deploying, e.g.
`https://your-app-name.onrender.com`

## Tech stack

- Python 3 + Django 4.2
- PostgreSQL
- HTML5 + Tailwind CSS (via CDN)
- Pillow (for handling uploaded images)

## Running it locally

```bash
git clone https://github.com/emmanuelopeto7-star/Django_photo_gallary.git
cd Django_photo_gallary
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt
```

Create a PostgreSQL database and user, e.g. with `psql`:

```sql
CREATE DATABASE photogallery_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE photogallery_db TO postgres;
```

`photogallery/settings.py` reads the DB name/user/password/host/port
from the environment variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`,
`DB_HOST`, `DB_PORT` (defaulting to `photogallery_db` / `postgres` /
`postgres` / `localhost` / `5432`). Set these to match your own
PostgreSQL setup, or edit the defaults directly in `settings.py`.
Never commit your real password to git.

Then run the app:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site, and `/admin/` to log in
as the superuser and add tags.

## Deploying to Render

1. Create a free account at [render.com](https://render.com).
2. Add a **PostgreSQL** database from the dashboard and note its
   connection details.
3. Add a **Web Service** connected to this GitHub repo, with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python manage.py migrate && gunicorn photogallery.wsgi`
     (add `gunicorn` to `requirements.txt` first)
4. Add environment variables for the database (`DB_NAME`, `DB_USER`,
   `DB_PASSWORD`, `DB_HOST`, `DB_PORT`) and a `DJANGO_SECRET_KEY`,
   then update `settings.py` to read `SECRET_KEY` and `ALLOWED_HOSTS`
   from the environment before deploying.
5. Deploy, then paste the live URL at the top of this README.
