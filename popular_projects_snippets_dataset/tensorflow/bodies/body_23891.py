# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
r"""Reads the next line, keeping \n. At EOF, returns ''."""
self._preread_check()
exit(self._prepare_value(self._read_buf.readline()))
