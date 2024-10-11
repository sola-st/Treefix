# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""synonym for save, to make it more file-like"""
self._save()
self._handles.close()
