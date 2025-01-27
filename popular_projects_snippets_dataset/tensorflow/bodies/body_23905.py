# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Deletes the path located at 'path'.

  Args:
    path: string, a path

  Raises:
    errors.OpError: Propagates any errors reported by the FileSystem API.  E.g.,
    `NotFoundError` if the path does not exist.
  """
_pywrap_file_io.DeleteFile(compat.path_to_bytes(path))
