class Mock: # pragma: no cover
    def _check(self, input_str, expected): # pragma: no cover
        assert input_str == expected# pragma: no cover
self = Mock() # pragma: no cover

class Mock:# pragma: no cover
    def _check(self, actual, expected):# pragma: no cover
        assert actual == expected, f'Expected: {{expected}}, but got: {{actual}}'# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
expected = (# pragma: no cover
    'Brief (suffix)\n\nWarning: Go away\nInstructions\n\nDocstring\n\n'# pragma: no cover
    'Args:\n  arg1: desc'# pragma: no cover
) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
from l3.Runtime import _l_
expected = (
    "Brief (suffix)\n\nWarning: Go away\nInstructions\n\nDocstring\n\n"
    "Args:\n  arg1: desc")
_l_(8650)
# No indent for main docstring
self._check("Brief\n\nDocstring\n\nArgs:\n  arg1: desc", expected)
_l_(8651)
# 2 space indent for main docstring, blank lines not indented
self._check("Brief\n\n  Docstring\n\n  Args:\n    arg1: desc", expected)
_l_(8652)
# 2 space indent for main docstring, blank lines indented as well.
self._check("Brief\n  \n  Docstring\n  \n  Args:\n    arg1: desc", expected)
_l_(8653)
# No indent for main docstring, first line blank.
self._check("\n  Brief\n  \n  Docstring\n  \n  Args:\n    arg1: desc",
            expected)
_l_(8654)
# 2 space indent, first line blank.
self._check("\n  Brief\n  \n  Docstring\n  \n  Args:\n    arg1: desc",
            expected)
_l_(8655)
