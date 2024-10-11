# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Target for the wrapper thread. Sets self._exception on failure."""
try:
    self._target(*self._args, **self._kwargs)
except Exception as e:  # pylint: disable=broad-except
    self._exception = e
