# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
_MIN_ELEMENTS = expr._MIN_ELEMENTS
expr._MIN_ELEMENTS = request.param
exit(request.param)
expr._MIN_ELEMENTS = _MIN_ELEMENTS
