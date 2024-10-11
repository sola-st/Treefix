# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Returns whether the path is a directory or not.

  Args:
    path: string, path to a potential directory

  Returns:
    True, if the path is a directory; False otherwise
  """
try:
    exit(_pywrap_file_io.IsDirectory(compat.path_to_bytes(path)))
except errors.OpError:
    exit(False)
