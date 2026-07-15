# Photo Gallery

A simple Django web app for browsing, uploading, tagging, and
liking/disliking photos. Built for a school assignment.

**Live demo:** TODO - add your Render URL here after deploying, e.g.
`https://your-app-name.onrender.com`

## Tech stack

- Python 3 + Django 5.2
- PostgreSQL
- HTML5 + Tailwind CSS (via CDN)
- Cloudinary (stores uploaded photos and profile pictures, so they
  survive redeploys on hosts with an ephemeral filesystem, like Render)

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
`postgres` / `localhost` / `5432`). The easiest way to set these is to
create a `.env` file in the project root:

```
DB_NAME=photogallery_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

It's loaded automatically and is already in `.gitignore`, so your
password never gets committed.

Photo uploads use Cloudinary. Create a free account at
[cloudinary.com](https://cloudinary.com), then copy your Cloud Name,
API Key, and API Secret from the dashboard into the same `.env` file:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

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
4. Add environment variables in the Render dashboard: `DB_NAME`,
   `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `CLOUDINARY_CLOUD_NAME`,
   `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, a random `SECRET_KEY`,
   `DEBUG=False`, and `ALLOWED_HOSTS` set to your Render domain (e.g.
   `your-app-name.onrender.com`). `settings.py` already reads all of
   these from the environment.
5. Deploy, then paste the live URL at the top of this README.
