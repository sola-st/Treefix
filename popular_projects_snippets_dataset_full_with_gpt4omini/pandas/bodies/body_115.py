# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 39140
with np.errstate(all="ignore"):
    expected = concat({name: op(string_series) for name, op in ops.items()})
    expected.name = string_series.name
    result = string_series.apply(ops)
    tm.assert_series_equal(result, expected)
