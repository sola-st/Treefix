# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if not self.is_open:
    raise ClosedFileError(f"{self._path} file is not open!")
