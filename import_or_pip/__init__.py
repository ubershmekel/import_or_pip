"""
import_or_pip is an easy way to import and make sure
your dependancies work.

In normal conditions you shouldn't
use this - just install whatever you need manually or
by a config file or something.

But I'm feeling lazy.
"""

import platform
import subprocess

def pip_install(name):
    if platform.system().lower() == 'linux':
        line = 'sudo pip install %s' % name
    else:
        line = 'pip install %s' % name

    subprocess.check_call(line, shell=True)


def import_or_pip(name, **kwargs):
    try:
        return __import__(name)
    except ImportError:
        pass
    if 'pip_name' in kwargs:
        name = kwargs['pip_name']

    pip_install(name)
    
    return __import__(name)
