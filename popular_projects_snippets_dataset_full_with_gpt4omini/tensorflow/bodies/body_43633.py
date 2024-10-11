# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
expected = "Nothing here\n\nWarning: Go away\nInstructions"
self._check(None, expected)
self._check("", expected)
