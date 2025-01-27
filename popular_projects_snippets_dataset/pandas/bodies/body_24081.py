# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
"""
        Reader using openpyxl engine.

        Parameters
        ----------
        filepath_or_buffer : str, path object or Workbook
            Object to be parsed.
        {storage_options}
        """
import_optional_dependency("openpyxl")
super().__init__(filepath_or_buffer, storage_options=storage_options)
