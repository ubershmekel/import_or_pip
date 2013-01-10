import unittest
import subprocess

from import_or_pip import import_or_pip

list_of_mods = ['py']

class TestImport(unittest.TestCase):
    def test_download(self):
        # make sure packages are removed first
        for name in list_of_mods:
            subprocess.call('sudo pip uninstall %s' % name, shell=True)
        for name in list_of_mods:
            try:
                __import__(name)
            except ImportError:
                pass
            else:
                raise Exception('Failed to remove packages before test')
        
        # try to import, should pip install
        for name in list_of_mods:
            mod = import_or_pip(name)

    def test_default(self):
        os1 = import_or_pip('os')
        import os
        self.assertEqual(os, os1)


if __name__ == "__main__":
    unittest.main()

