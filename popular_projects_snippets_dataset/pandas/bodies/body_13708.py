# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# test gmap given as DataFrame that it aligns to the data including subset
expected = styler_blank.background_gradient(axis=None, gmap=exp_gmap, subset=subset)
result = styler_blank.background_gradient(axis=None, gmap=gmap, subset=subset)
assert expected._compute().ctx == result._compute().ctx
