# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_missing.py
# GH 40250
df = DataFrame({"a": pd.array([None, "a", None], dtype="string"), "b": [0, 0, 0]})
grp = df.groupby("b")
result = grp.fillna(method=method)
expected = DataFrame({"a": pd.array(expected, dtype="string")})
tm.assert_frame_equal(result, expected)
