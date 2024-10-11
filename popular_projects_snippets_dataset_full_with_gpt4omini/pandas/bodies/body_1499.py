# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
df = DataFrame(np.random.randn(4, 4), index=list("abcd"), columns=list("ABCD"))

result = df.iloc[0, 0]

df.loc["a", "A"] = 1
result = df.loc["a", "A"]
assert result == 1

result = df.iloc[0, 0]
assert result == 1

df.loc[:, "B":"D"] = 0
expected = df.loc[:, "B":"D"]
result = df.iloc[:, 1:]
tm.assert_frame_equal(result, expected)
