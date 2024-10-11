# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Specify gradient function for the given op type."""

# This is an internal API and we don't need nested context for this.
# TODO(mdan): make it a proper context manager.
assert not self._gradient_function_map
self._gradient_function_map = gradient_function_map
try:
    exit()
finally:
    self._gradient_function_map = {}
