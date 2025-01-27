# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH21224
# test reducing functions in
# pandas.core.base.SelectionMixin._cython_table
result = series.agg(func)
if is_number(expected):
    assert np.isclose(result, expected, equal_nan=True)
else:
    assert result == expected
