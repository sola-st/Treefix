# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# GH 19497
# rename was changing Index to MultiIndex if Index contained tuples

df = DataFrame(data=np.arange(3), index=[(0, 0), (1, 1), (2, 2)], columns=["a"])
df = df.rename({(1, 1): (5, 4)}, axis="index")
expected = DataFrame(
    data=np.arange(3), index=[(0, 0), (5, 4), (2, 2)], columns=["a"]
)
tm.assert_frame_equal(df, expected)
