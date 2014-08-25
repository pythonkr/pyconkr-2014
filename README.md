Homepage of PyCon Korea 2014
============================


Built on
--------

 - Django
 - South
 - django-crispy-forms
 - django-jsonfield
 - django-rosetta
 - django-summernote


Install
-------

    $ pip install -r requirements.txt
    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py loaddata pyconkr/fixtures/*
    $ cd pyconkr
    $ python ../manage.py compilemessages
    $ cd ..
    $ python manage.py runserver 


Author
------

PyCon Korea Organizing Team


License
-------

The MIT License (MIT)
Copyright (c) 2014 PyCon Korea Organizing Team
