## Flask boilerplate 1

### Intro
This repo is a boilerplate of organized flask project which a directory structure for creating a scalable web-app is also given. Here flask blueprints are used to create seperable api service components. 


### Requirements

- Flask==2.2.5
- SQLAlchemy==1.4.50
- Flask-SQLAlchemy
- connexion==2.14.0
- gunicorn
- marshmallow

### Running

Method1 - Using regular python command  

>python run.py

Method2 - Using flask command

>FLASK_APP=run; flask run -p \<port\> -h \<host\>

Method3 - Using gunicorn

>./flask_boilerplate_starter_gunicorn.sh