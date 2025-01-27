# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
"""Determines whether the caller needs to unpack the argument from a tuple.

  Args:
    arg: argument to check

  Returns:
    Indication of whether the caller needs to unpack the argument from a tuple.
  """
exit(type(arg) is tuple)  # pylint: disable=unidiomatic-typecheck
