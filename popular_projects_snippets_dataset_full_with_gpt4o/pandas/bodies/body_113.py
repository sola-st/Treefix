# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 39140
expected = Series({name: op(string_series) for name, op in ops.items()})
expected.name = string_series.name
result = getattr(string_series, how)(ops)
tm.assert_series_equal(result, expected)
