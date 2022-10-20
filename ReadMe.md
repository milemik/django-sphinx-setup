# Django Sphinx setup

Just a simple and basic setup of sphinx with django :)


## How to

### Install dependencies

1. Install poetry: ```pip install poetry ```
2. Install dependencies: ```poetry install```


### Setup django

1. Run migration: ```python manage.py migrate```


### Create sphinx documentation

1. Create/Update sphinx: ```cd docs && make html && cd ..```


### Update sphinx

If you add some new file you need to update his rst file in docs.
Example:

if you create new file in users app named utils, you will need to update
users.rst file and add following:
``` rst
users.utils module
------------------

.. automodule:: users.utils
   :members:
   :undoc-members:
   :show-inheritance:
```

Then you need again to cd into doc directory and run ```make html```

After this if you open index.html from docs/_build/html directory
your documentation will be updated
