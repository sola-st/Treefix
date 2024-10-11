# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
expected = "Brief (suffix)\n\nWarning: Go away\nInstructions\n\nDocstring"
# No second line indent
self._check("Brief\nDocstring", expected)
# 2 space second line indent
self._check("Brief\n  Docstring", expected)
# No second line indent, first line blank
self._check("\nBrief\nDocstring", expected)
# 2 space second line indent, first line blank
self._check("\n  Brief\n  Docstring", expected)
