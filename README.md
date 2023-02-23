# TestProject

## Running with docker

```
git clone <github_project_path>

cd TestProject

docker-compose run web python3.10 manage.py createcachetable

docker-compose run web python3.10 manage.py migrate #migrate django db inside container

docker-compose up

# If the server is running successfully at http://0.0.0.0:8000/ consider the backned is up

```

### Import the CSV Data to django models
```
# Open termimnal and execute the folling commands to import data from csv

python3.10 utilities/load_csv_into_db.py -file path test_app/data_source/Project_raw_table.csv -model project

python3.10 utilities/load_csv_into_db.py -file_path test_app/data_source/WTG_raw_table.csv -model wtg
```

### Run the User Interface
```
# Open terminal and run the server on current folder using following command

$ python3.10 -m http.server 80

Then open index.html from the http://localhost:80
```

### Developed and Tested using below backend tools, technologies, frameworks or modules:
```
    OS: macOS Monterey 12.0.1
    IDE: PyCharm 2021.2.1 (Community Edition)
    Python: 3.10
    django: 4.1.7
    DB: Sqlite3
    djangorestframework: 3.14.0
    drf-api-logger: 1.1.2
    pands: 1.5.3
```


### Run DB Migrations

```
$ python3.10 manage.py makemigrations

$ python3.10 manage.py migrate

$ python3.10 manage.py createcachetable

$ python3.10 manage.py createsuperuser

```