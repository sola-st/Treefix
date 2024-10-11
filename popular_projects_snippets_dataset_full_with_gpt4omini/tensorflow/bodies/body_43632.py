# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
expected = "Brief (suffix)\n\nWarning: Go away\nInstructions"
self._check("Brief", expected)
self._check("Brief\n", expected)
self._check("Brief\n  ", expected)
self._check("\nBrief\n  ", expected)
self._check("\n  Brief\n  ", expected)
