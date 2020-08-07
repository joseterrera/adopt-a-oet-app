Below are the steps that should get one started using the app:

### Create a Virtual Environment

```console
$ python3 -m venv venv
$ source venv/bin/activate
```


### Create a database

```console
createdb adopt
```



### Packages installed
```console
$ pip3 install flask  
$ pip3 install flask-debugtoolbar   
$ pip3 install psycopg2-binary    
$ pip3 install flask-sqlalchemy
$ pip3 install flask_wtf
$ pip3 freeze > requirements.txt
```

### To run the app:

```console
flask run 
```