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
import re

version = '0.2'
if platform.system().lower() == 'linux':
    pip_exe = 'sudo pip'
else:
    pip_exe = 'pip'


def pip_install(name):
    line = pip_exe + ' install %s' % name
    subprocess.check_call(line, shell=True)

def remove_pip_versioning(name):
    """
    to allow importing e.g. "arff==0.7" ==> "arff"
    """
    return re.sub(r'([=><].*)', '', name)

def import_or_pip(name, **kwargs):
    try:
        return __import__(name)
    except ImportError:
        pass
    if 'pip_name' in kwargs:
        name = kwargs['pip_name']

    pip_install(name)
    clean_name = remove_pip_versioning(name)
    # TODO: check for the correct version with pkg_resources and avoid
    # pip_install subprocess if we already have it.
    return __import__(clean_name)

