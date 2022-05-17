# Simple Web application

Created using
- Flask 
- Bootstrap
- PostgreSQL

## Steps to run

Build the image:
```bash
$ docker-compose build
```

Create the tables in Postgres
```bash
$ docker-compose exec web python manage.py create_db
```
Once the image is built, run the container:
```bash
$ docker-compose up -d
```

## Run the application
Try http://localhost:5000/

## Verification

To check the database tables

Open psql
```bash
$ docker-compose exec db psql --username=simple_web_form --dbname=simple_web_form
```
Connect to database
```bash
\c simple_web_form
```
Query the table
```bash
select * from contacts;
```
Quit
```bash
\q
```

