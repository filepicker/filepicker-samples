Example of using filepicker.io with Django
==========================================

Requirments:

* python 2.7
* Django 1.7
* django-filepicker 0.2.1

Configuration of filepicker API KEY
-----------------------------------

    Insert API KEY to file *filepicker_demo/settigs.py* to FILE_PICKER_API_KEY variable


Running appliction
-----------------------------------
    
    Database initialization:
    python manage.py migrate
    
    Create admin user:
    python manage.py createsuperuser
    
    Start demo application:
    python manage.py runserver

    application will be available on http://localhost:8000/
    admin panel will be available on http://localhost:8000/admin