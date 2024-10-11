# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 16114
result = Series(name=0, dtype=object).to_frame().dtypes
expected = Series({0: object})
tm.assert_series_equal(result, expected)

result = DataFrame(Series(name=0, dtype=object)).dtypes
tm.assert_series_equal(result, expected)
