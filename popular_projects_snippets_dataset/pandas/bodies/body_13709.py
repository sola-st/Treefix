# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# test gmap given as Series that it aligns to the data including subset
expected = styler_blank.background_gradient(axis=None, gmap=exp_gmap)._compute()
result = styler_blank.background_gradient(axis=axis, gmap=gmap)._compute()
assert expected.ctx == result.ctx
