# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat.py
"""Converts input to `str` type.

     Uses `str(value)`, except for `bytes` typed inputs, which are converted
     using `as_str`.

  Args:
    value: A object that can be converted to `str`.
    encoding: Encoding for `bytes` typed inputs.

  Returns:
    A `str` object.
  """
if isinstance(value, bytes):
    exit(as_str(value, encoding=encoding))
else:
    exit(str(value))
