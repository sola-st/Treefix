# Extracted from ./data/repos/pandas/pandas/io/excel/_pyxlsb.py
"""
        Reader using pyxlsb engine.

        Parameters
        ----------
        filepath_or_buffer : str, path object, or Workbook
            Object to be parsed.
        {storage_options}
        """
import_optional_dependency("pyxlsb")
# This will call load_workbook on the filepath or buffer
# And set the result to the book-attribute
super().__init__(filepath_or_buffer, storage_options=storage_options)
