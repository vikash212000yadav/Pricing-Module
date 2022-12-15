# Pricing Module

Pricing Module is based on Django web framework.

## Steps to install and run in local system:-

- Create a virtual environment
    ```python3 -m venv <env_name>```
    
- Activate virtual environment
    ```source <env_name>/bin/activate```
    
- Install requirements in venv
    ```pip install -r requirements.txt```
    
- Make migrations
    ```python manage.py makemigrations```
    
- Apply migrations
    ```python manage.py migrate``` 
    
- Create a super user
    ```python manage.py createsuperuser``` 
    
- Run the server
    ```python manage.py runserver``` 

- To test the API run
    ```localhost/price/<id>```

    
<small>You can delete db.sqlite3 and then make your own migrations further.</small>