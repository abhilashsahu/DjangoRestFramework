# TestProject

### Deploy the backend instance using docker
```
git clone git@github.com:abhilashsahu/DjangoRestFramework.git

docker-compose run web python3.10 manage.py migrate #migrate django db inside container

docker-compose run web python3.10 manage.py createcachetable

docker-compose up

# If the server is running successfully at http://0.0.0.0:8000/ consider the backned is up
Check the URL: http://0.0.0.0:8000/test_app/v1/projects/

```

### Load the data into DB
```
# Open a termimnal, traverse to project directory and execute the folling commands to import data from csv

python utilities/load_csv_into_db.py -file_path test_app/data_source/Project_raw_table.csv -model project

python utilities/load_csv_into_db.py -file_path test_app/data_source/WTG_raw_table.csv -model wtg

```

### Run the User Interface
```
# Open a termimnal, traverse to project directory and run the server for frontent using following command

python -m http.server 80

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
    Jquery, Bootstrap, JavaScript fetch, etc
 
```


### Run DB Migrations
```
python3.10 manage.py makemigrations

python3.10 manage.py migrate

python3.10 manage.py createcachetable

python3.10 manage.py createsuperuser

```
