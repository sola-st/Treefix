# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame({"a": [2, 3, 1], "b": [2, 1, 1], "c": list("xyx")})
if numeric_only:
    result = df.idxmin(numeric_only=numeric_only)
    expected = Series([2, 1], index=["a", "b"])
    tm.assert_series_equal(result, expected)
else:
    with pytest.raises(TypeError, match="not allowed for this dtype"):
        df.idxmin(numeric_only=numeric_only)
