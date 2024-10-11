# Extracted from ./data/repos/pandas/pandas/io/excel/_xlrd.py
"""
        Reader using xlrd engine.

        Parameters
        ----------
        filepath_or_buffer : str, path object or Workbook
            Object to be parsed.
        {storage_options}
        """
err_msg = "Install xlrd >= 2.0.1 for xls Excel support"
import_optional_dependency("xlrd", extra=err_msg)
super().__init__(filepath_or_buffer, storage_options=storage_options)
