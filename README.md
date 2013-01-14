import_or_pip
=============

A python module that lets you import a module or pip install it if it isn't found

E.g.

    from import_or_pip import import_or_pip
    jinja2 = import_or_pip('jinja2')
    # jinja2 is imported if it's already installed
    # but if the import fails - pip install jinja2 is executed

And import_or_pip will just import if jinja2 is installed.download your dependancy if it isn't already installed.

To install import_or_pip run:

    pip install import_or_pip

or download the package from github/pypi and run:

    python setup.py install


What about buildout or pip -r requirements.txt
=============
Those are better solutions - use them! This is more of a toy for interactive
sessions and probably not the right tool for many projects because installing
is a big deal that shouldn't just happen on its own. Though it is useful on
some occasions.


Tested on Ubuntu and Windows with python 2.7 and 3.3