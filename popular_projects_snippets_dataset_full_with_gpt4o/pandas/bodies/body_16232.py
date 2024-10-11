# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#9016: support bitwise op for integer types
s_0123 = Series(range(4), dtype="int64")

result = s_0123 & Series([False, np.NaN, False, False])
expected = Series([False] * 4)
tm.assert_series_equal(result, expected)

s_abNd = Series(["a", "b", np.NaN, "d"])
with pytest.raises(TypeError, match="unsupported.* 'int' and 'str'"):
    s_0123 & s_abNd
