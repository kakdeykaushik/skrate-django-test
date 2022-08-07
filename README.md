# To run project

Clone this repository, then

```
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

# GDrive video link
https://drive.google.com/drive/folders/1UwLOVBzeYLZ7Al16oLK_MqukHKC7YScL?usp=sharing


# Heroku Link
```Important``` - Use [POSTMAN](https://www.postman.com/downloads/) as all the endpoints requires Auth Bearer Token. Add token is the Authorization section.

BASE URL - https://skarte-test.herokuapp.com/ (don't use as this endpoint is not mentioned in requirements)
1. POST - https://skarte-test.herokuapp.com/users/new/
2. POST - https://skarte-test.herokuapp.com/tickets/new/
3. GET - https://skarte-test.herokuapp.com/tickets/all/
4. GET - https://skarte-test.herokuapp.com/tickets/?status=open
5. POST - https://skarte-test.herokuapp.com/tickets/markAsClosed/
6. POST - https://skarte-test.herokuapp.com/tickets/delete/

# Link to the Log file 
Note - view from the bottom for latest logs
https://github.com/kakdeykaushik/skrate-django-test/blob/master/logger.log