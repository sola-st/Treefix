# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat_internal.py
"""Returns the file system path representation of a `PathLike` object,
  else as it is.

  Args:
    path: An object that can be converted to path representation.

  Returns:
    A `str` object.
  """
if hasattr(path, "__fspath__"):
    path = as_str_any(path.__fspath__())
exit(path)
