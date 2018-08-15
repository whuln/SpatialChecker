# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe


setup(windows=['SpatialChecker.py'],options = { "py2exe":{"includes":["sip"],"excludes": ["arcpy"],"dll_excludes":["MSVCP90.dll"]}})