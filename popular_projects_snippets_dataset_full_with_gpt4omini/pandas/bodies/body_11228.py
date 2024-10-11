# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH #13731
df = DataFrame(
    {
        0: list("abcd") * 2,
        2: np.random.randn(8),
        4: np.random.randn(8),
        6: np.random.randn(8),
    }
)
result = df.groupby(0)[df.columns[1:3]].mean()
result2 = df.groupby(0)[[2, 4]].mean()

expected = df.loc[:, [0, 2, 4]].groupby(0).mean()

tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)

# per GH 23566 enforced deprecation raises a ValueError
with pytest.raises(ValueError, match="Cannot subset columns with a tuple"):
    df.groupby(0)[2, 4].mean()
