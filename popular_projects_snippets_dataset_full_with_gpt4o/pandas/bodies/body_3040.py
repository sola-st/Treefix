# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_compare.py
# test DataFrames with different indices
msg = (
    r"Can only compare identically-labeled \(both index and columns\) DataFrame "
    "objects"
)
with pytest.raises(ValueError, match=msg):
    df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"])
    df2 = pd.DataFrame([1, 2, 3], index=["a", "b", "d"])
    df1.compare(df2)

# test DataFrames with different shapes
msg = (
    r"Can only compare identically-labeled \(both index and columns\) DataFrame "
    "objects"
)
with pytest.raises(ValueError, match=msg):
    df1 = pd.DataFrame(np.ones((3, 3)))
    df2 = pd.DataFrame(np.zeros((2, 1)))
    df1.compare(df2)
