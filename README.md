## Summary

Orange County Lettings web site

## Local Development

### Prerequisite

- Github account with write access to this repository
- Git CLI
- SQLite3 CLI
- Python Interpreter, version 3.6 or higher
- Sentry account
- Dockerhub account
- Heroku account
- Access to the CircleCI project `oc-lettings-site`

The rest of the local development documentation assumes the command `python` in your OS shell runs the above Python interpreter (unless a virtual environment is activated)

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/AdrienB-OC/projet-13.git`

#### Setup the virtual environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step has package not found errors on Ubuntu)
- Activate the virtual environment `source venv/bin/activate`
- Confirm the `python` command runs the virtual environment's Python interpreter `which python`
- Confirm the Python interpreter version is >= 3.6 `python --version`
- Confirm the `pip` command runs the virtual environment's pip `which pip`
- To deactivate the virtual environment `deactivate`

#### Environment Variables

Create a .env file in the project folder root and add the following :  
`SECRET_KEY=<project's secret key>`
`SENTRY_DSN=<your sentry project's dsn>`


#### Run the site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://127.0.0.1:8000` or `http://localhost:8000` in the browser of your choice.
- Confirm the site is working and can be navigated (you should be able to see multiple profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables from the database `.tables`
- Display columns in the profiles table `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profiles table `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- CLogin with username `admin`, password `Abc1234!`

### Windows

PowerShell usage as described above except :

- To activate the virtual environment `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`


## Deployment
This assumes you already have the containerization in place in your CircleCI project and have created a sentry project.
- On the heroku website :
  - Get your <API key> from `https://dashboard.heroku.com/account`
  - Create a new app <App Name>
  - Go the app's settings and in the Config Vars section click Reveal Config Vars and add the following variables with the corresponding values :
    - `SECRET_KEY` - The django project's SECRET_KEY
    - `SENTRY_DSN` - Your sentry project's DSN
  
- In the CircleCi project, go to settings and add the following Environment Variables :
  - `HEROKU_API_KEY` - <API key>
  - `HEROKU_APP_NAME` - <App Name>  (The CircleCI project should now have the following Environment Variables : `DOCKERHUB_USERNAME`, `DOCKERHUB_PASSWORD`, `SECRET_KEY`, `SENTRY_DSN`, `HEROKU_API_KEY`, `HEROKU_APP_NAME`  
  - Trigger a build in CircleCI
  
- Go to `https://<App Name>.herokuapp.com` in the browser of your choice and confirm the site is running properly
- Go to `https://<App Name>.herokuapp.com/test` to trigger an error that shoud be sent to your Sentry project
- Go to `https://<App Name>.herokuapp.com/admin` to try the login to the admin panel using the same admin credentials
  

## Containerization
You can run the site locally from a command prompt using the following command after you logged into docker using `docker login`:  
  `docker run --env-file .env --rm --publish 8000:8000 docker-user/docker-project:tag`  
Your command should look like this in practice:  
  `docker run --env-file .env --rm --publish 8000:8000 fnrl023/projet-13:3ffccc26d559065e59784bb6974b6ad31e014c65`
  
You need to have a .env file with the SECRET_KEY and SENTRY_DSN values in your current folder when running this command.
