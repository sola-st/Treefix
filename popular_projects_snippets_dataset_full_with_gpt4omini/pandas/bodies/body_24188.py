# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
"""
        Save workbook to disk.
        """
for sheet in self.sheets.values():
    self.book.spreadsheet.addElement(sheet)
self.book.save(self._handles.handle)
