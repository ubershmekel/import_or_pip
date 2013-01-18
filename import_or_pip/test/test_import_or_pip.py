import unittest
import subprocess
import sys

import import_or_pip as pimp

list_of_mods = ['arff']

class TestImport(unittest.TestCase):
    def test_download(self):
        # make sure packages are removed first
        for name in list_of_mods:
            subprocess.call(pimp.pip_exe + ' uninstall %s' % name, shell=True)
        for name in list_of_mods:
            try:
                __import__(name)
            except ImportError:
                pass
            else:
                raise Exception('Failed to remove packages before test')
        
        # try to import, should pip install
        for name in list_of_mods:
            mod = pimp.import_or_pip(name)

    def test_default(self):
        os1 = pimp.import_or_pip('os')
        import os
        self.assertEqual(os, os1)

    def test_version_import(self):
        py = pimp.import_or_pip('py==1.4.0')
        self.assertEqual(py.version, '1.4.0')
        

if __name__ == "__main__":
    unittest.main()

