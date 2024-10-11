# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH41170
ser = Series(
    range(len(values[0])), index=MultiIndex.from_arrays(values), dtype="object"
)
result = ser.reindex(np.array(["b"]), level=0)
expected = Series(
    index=MultiIndex(levels=[["b"], values[1]], codes=[[], []]), dtype="object"
)
tm.assert_series_equal(result, expected)
