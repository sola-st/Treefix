# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Checks whether the file system supports atomic moves.

  Returns whether or not the file system of the given path supports the atomic
  move operation for a file or folder.  If atomic move is supported, it is
  recommended to use a temp location for writing and then move to the final
  location.

  Args:
    path: string, path to a file

  Returns:
    True, if the path is on a file system that supports atomic move
    False, if the file system does not support atomic move. In such cases
           we need to be careful about using moves. In some cases it is safer
           not to use temporary locations in this case.
  """
try:
    exit(_pywrap_file_io.HasAtomicMove(compat.path_to_bytes(path)))
except errors.OpError:
    # defaults to True
    exit(True)
