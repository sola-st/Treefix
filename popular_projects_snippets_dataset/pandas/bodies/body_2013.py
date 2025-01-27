# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH 32394
result = to_numeric("uint64", errors="coerce")
assert np.isnan(result)

ser = Series([32, 64, np.nan])
result = to_numeric(Series(["32", "64", "uint64"]), errors="coerce")
tm.assert_series_equal(result, ser)
