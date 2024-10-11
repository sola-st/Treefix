# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""
        Save workbook to disk.
        """
self.book.save(self._handles.handle)
if "r+" in self._mode and not isinstance(self._handles.handle, mmap.mmap):
    # truncate file to the written content
    self._handles.handle.truncate()
