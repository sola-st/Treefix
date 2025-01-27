# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Writes file_content to the file. Appends to the end of the file."""
self._prewrite_check()
self._writable_file.append(
    compat.as_bytes(file_content, encoding=self.__encoding))
