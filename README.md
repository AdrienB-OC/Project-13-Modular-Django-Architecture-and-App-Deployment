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
