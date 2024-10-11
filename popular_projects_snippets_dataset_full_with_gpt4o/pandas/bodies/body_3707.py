# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#18570
df = DataFrame(
    {"a": [1, 4, 3, 2], "b": [4, 6, 7, 3], "c": ["a", "b", "c", "d"]}
)
s = Series([0, 6, 7, 3])
if numeric_only:
    result = df.corrwith(s, numeric_only=numeric_only)
    corrs = [df["a"].corr(s), df["b"].corr(s)]
    expected = Series(data=corrs, index=["a", "b"])
    tm.assert_series_equal(result, expected)
else:
    with pytest.raises(
        TypeError,
        match=r"unsupported operand type\(s\) for /: 'str' and 'int'",
    ):
        df.corrwith(s, numeric_only=numeric_only)
