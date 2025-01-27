# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        If we opened a stream earlier, in _get_data_from_filepath, we should
        close it.

        If an open stream or file was passed, we leave it open.
        """
if self.handles is not None:
    self.handles.close()
