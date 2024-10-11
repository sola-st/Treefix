# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
if not self._read_buf:
    if not self._read_check_passed:
        raise errors.PermissionDeniedError(None, None,
                                           "File isn't open for reading")
    self._read_buf = _pywrap_file_io.BufferedInputStream(
        compat.path_to_str(self.__name), 1024 * 512)
