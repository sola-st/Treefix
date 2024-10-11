# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Close the file if it was created by the writer.

        If a buffer or file-like object was passed in, for example a GzipFile,
        then leave this file open for the caller to close.
        """
# write compression
if self._output_file is not None:
    assert isinstance(self.handles.handle, BytesIO)
    bio, self.handles.handle = self.handles.handle, self._output_file
    self.handles.handle.write(bio.getvalue())
