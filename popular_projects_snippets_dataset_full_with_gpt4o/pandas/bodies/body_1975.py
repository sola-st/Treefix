# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-16302
ser = Series([], dtype=object)
result = to_numeric(ser, **input_kwargs)

expected = Series([], **result_kwargs)
tm.assert_series_equal(result, expected)
