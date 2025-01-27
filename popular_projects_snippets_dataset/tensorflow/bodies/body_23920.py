# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Deletes everything under path recursively.

  Args:
    path: string, a path

  Raises:
    errors.OpError: If the operation fails.
  """
_pywrap_file_io.DeleteRecursively(compat.path_to_bytes(path))
