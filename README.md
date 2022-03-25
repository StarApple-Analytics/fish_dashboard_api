# Fishes Dashboard API

Tool to monitor data analyzed from Fishes Dataset

## Installation

Create virtual python environment and install dependencies located in pip file

```bash
$ pipenv shell
$ pipenv install
```

Copy environment variables through .env.example and configure them

```bash
$ cp .env.example .env
```







## Setting Flask app

Set Flask App on CMD

```bash
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=true # Enable debugging
```

## Migrating Database

Migration files are responsible for managing the currently configured database, ensuring that stored tables matches the app's data models. 
The migration files are located in the migration folder, ensure that you have set the Database URI in the ```.env``` file

Run Migrations

```
$ flask db upgrade
```


Running Flask app

```bash
$ flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

