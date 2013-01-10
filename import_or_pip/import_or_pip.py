import subprocess

def import_or_pip(name, **kwargs):
    """
    import_or_pip is an easy way to import and make sure
    your dependancies work.

    In normal conditions you shouldn't
    use this - just install whatever you need manually or
    by a config file or something.

    But I'm feeling lazy.
    """
    try:
        return __import__(name)
    except ImportError:
        pass
    if 'pip_name' in kwargs:
        name = kwargs['pip_name']
    line = 'sudo pip install %s' % name
    subprocess.call(line, shell=True)

    return __import__(name)
