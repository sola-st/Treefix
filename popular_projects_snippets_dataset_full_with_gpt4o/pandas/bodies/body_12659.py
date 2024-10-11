# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH31464
result = read_json("[true, true, false]", typ="series")
expected = Series([True, True, False])
tm.assert_series_equal(result, expected)
