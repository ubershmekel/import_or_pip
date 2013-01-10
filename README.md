import_or_pip
=============

A python module that lets you import a module or pip install it if it isn't found

E.g.

    from import_or_pip import import_or_pip
    jinja2 = import_or_pip('jinja2')
    # jinja2 is just imported if it's installed
    # but if the import fails - pip install jinja2 is executed

And import_or_pip will just import if jinja2 is installed.download your dependancy if it isn't already installed.

Note that this is probably not the right way to work in many projects because
installing is a big deal that shouldn't just happen on its own. But I find it
useful.

