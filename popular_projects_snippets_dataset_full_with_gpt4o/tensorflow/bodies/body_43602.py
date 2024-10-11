# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat.py
r"""Converts input which is a `PathLike` object to `bytes`.

  Converts from any python constant representation of a `PathLike` object
  or `str` to bytes.

  Args:
    path: An object that can be converted to path representation.

  Returns:
    A `bytes` object.

  Usage:
    In case a simplified `bytes` version of the path is needed from an
    `os.PathLike` object.
  """
if hasattr(path, '__fspath__'):
    path = path.__fspath__()
exit(as_bytes(path))
