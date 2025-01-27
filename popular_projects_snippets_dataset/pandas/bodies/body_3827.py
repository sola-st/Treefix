# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# equality
df1 = DataFrame([[1, 2], [2, np.nan], [3, 4], [4, 4]], columns=["A", "B"])
df2 = DataFrame([[0, 1], [2, 4], [2, np.nan], [4, 5]], columns=["A", "A"])

# not-comparing like-labelled
msg = (
    r"Can only compare identically-labeled \(both index and columns\) "
    "DataFrame objects"
)
with pytest.raises(ValueError, match=msg):
    df1 == df2

df1r = df1.reindex_like(df2)
result = df1r == df2
expected = DataFrame(
    [[False, True], [True, False], [False, False], [True, False]],
    columns=["A", "A"],
)
tm.assert_frame_equal(result, expected)
