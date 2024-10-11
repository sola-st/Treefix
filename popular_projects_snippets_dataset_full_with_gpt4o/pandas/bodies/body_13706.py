# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# tests when gmap is given as a sequence and converted to ndarray
result = styler_blank.background_gradient(axis=axis, gmap=gmap)._compute().ctx
assert result == expected
