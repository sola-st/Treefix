# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 39140
expected = Series({name: op(string_series) for name, op in zip(names, ops)})
expected.name = "series"
result = getattr(string_series, how)(ops)
tm.assert_series_equal(result, expected)
