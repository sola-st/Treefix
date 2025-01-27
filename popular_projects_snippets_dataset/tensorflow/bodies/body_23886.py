# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
if self._binary_mode:
    exit(compat.as_bytes(val, encoding=self.__encoding))
else:
    exit(compat.as_str_any(val, encoding=self.__encoding))
