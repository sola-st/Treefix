# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
if not self._writable_file:
    if not self._write_check_passed:
        raise errors.PermissionDeniedError(None, None,
                                           "File isn't open for writing")
    self._writable_file = _pywrap_file_io.WritableFile(
        compat.path_to_bytes(self.__name), compat.as_bytes(self.__mode))
