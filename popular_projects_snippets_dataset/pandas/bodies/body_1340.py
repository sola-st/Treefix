# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# try with labelled frame
df = DataFrame(
    np.random.randn(10, 4), index=list("abcdefghij"), columns=list("ABCD")
)

result = df.iloc[1, 1]
exp = df.loc["b", "B"]
assert result == exp

result = df.iloc[:, 2:3]
expected = df.loc[:, ["C"]]
tm.assert_frame_equal(result, expected)

# negative indexing
result = df.iloc[-1, -1]
exp = df.loc["j", "D"]
assert result == exp

# out-of-bounds exception
msg = "index 5 is out of bounds for axis 0 with size 4"
with pytest.raises(IndexError, match=msg):
    df.iloc[10, 5]

# trying to use a label
msg = (
    r"Location based indexing can only have \[integer, integer "
    r"slice \(START point is INCLUDED, END point is EXCLUDED\), "
    r"listlike of integers, boolean array\] types"
)
with pytest.raises(ValueError, match=msg):
    df.iloc["j", "D"]
