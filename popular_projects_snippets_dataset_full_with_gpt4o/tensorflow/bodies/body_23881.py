# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
self.__name = name
self.__mode = mode
self.__encoding = encoding
self._read_buf = None
self._writable_file = None
self._binary_mode = "b" in mode
mode = mode.replace("b", "")
if mode not in ("r", "w", "a", "r+", "w+", "a+"):
    raise errors.InvalidArgumentError(
        None, None, "mode is not 'r' or 'w' or 'a' or 'r+' or 'w+' or 'a+'")
self._read_check_passed = mode in ("r", "r+", "a+", "w+")
self._write_check_passed = mode in ("a", "w", "r+", "a+", "w+")
