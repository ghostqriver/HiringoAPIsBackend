HiringoAPIsBackend
===
Launch the project
---
In the project directory, run the project using: python manage.py runserver,

then you can view the service at: http://127.0.0.1:8000/

if you do any modified on the codes if will reload automatically.

And by modifying the setting.py, you can also change the connection information of database:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hiringo',
        'USER': 'root',
        'PASSWORD': '996561',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

APIs descriptions
---
At the mainpage http://127.0.0.1:8000/ , you can see all the urls of different APIs
    For example:
    http://127.0.0.1:8000/courses/ to create or list all the courses, 
    http://127.0.0.1:8000/courses/{transaction_id}/ to read and modify the specific course with the transaction_id.
    
By the page http://127.0.0.1:8000/docs/ , you can find more details.

The Administration Page
---
Here is another backend admin page: http://127.0.0.1:8000/admin (Account:admin Password:123456hiringo) to deal with all the infomations in the backend.
