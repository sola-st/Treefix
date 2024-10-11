# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/io_utils.py
"""Convert `PathLike` objects to their string representation.

  If given a non-string typed path object, converts it to its string
  representation.

  If the object passed to `path` is not among the above, then it is
  returned unchanged. This allows e.g. passthrough of file objects
  through this function.

  Args:
    path: `PathLike` object that represents a path

  Returns:
    A string representation of the path argument, if Python support exists.
  """
if isinstance(path, os.PathLike):
    exit(os.fspath(path))
exit(path)
