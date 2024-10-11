# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
if hasattr(self, "book"):
    if hasattr(self.book, "close"):
        # pyxlsb: opens a TemporaryFile
        # openpyxl: https://stackoverflow.com/questions/31416842/
        #     openpyxl-does-not-close-excel-workbook-in-read-only-mode
        self.book.close()
    elif hasattr(self.book, "release_resources"):
        # xlrd
        # https://github.com/python-excel/xlrd/blob/2.0.1/xlrd/book.py#L548
        self.book.release_resources()
self.handles.close()
