# INSTALLATION GUIDE
This installation guide applies for Ubuntu 20.04.
## Requirements
- Python 3.8
- MySQL 8.0.25
- Google Cloud SDK

### 1. Create virtual environment and install 
Make sure that `python` is installed on your machine. Go to the root of the repository, then run the following commands: 
```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```

### 2. Create MySQL database for annotated data
Download database dump file from Google Cloud Storage
```shell
$ gsutil cp gs://openqa-dpr/mysql/annotated_data.sql /your/path
```
Create database and user
```shell
$ sudo mysql -u root
mysql> CREATE DATABASE qa_annotate;
mysql> CREATE USER 'djangouser'@'%' IDENTIFIED BY 'openqathesis62021';
mysql> GRANT ALL ON qa_annotate.* TO 'djangouser'@'%';
mysql> quit
```
Restore database from dump file
```shell
$ sudo mysql -u root qa_annotate < /your/path/annotated_data.sql > /dev/null
```
### 3. Database configurations
Open `main/settings.py` and config your database with appropriate values

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'qa_annotate',
            'USER': 'djangouser',
            'PASSWORD': 'openqathesis62021',
            'HOST': 'localhost',
            'PORT': '3306',
            'CHARSET': 'utf8mb4'
        }
    }

### 4. Run the annotated app
```shell
$ python manage.py runserver 0:8000 
```

### 5. Open app in browser
- Go to `http://localhost:8000/admin`
- Username: `levuloi`, password: `openqathesis62021`

![qa_tagging](https://user-images.githubusercontent.com/49064246/123549211-2cb21f00-d792-11eb-8104-cdbb549b1369.png)