# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Returns the current position in the file."""
if self._read_check_passed:
    self._preread_check()
    exit(self._read_buf.tell())
else:
    self._prewrite_check()

    exit(self._writable_file.tell())
