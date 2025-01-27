# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# GH6296
# iloc should allow indexers that exceed the bounds
df = DataFrame(np.random.random_sample((20, 5)), columns=list("ABCDE"))

# lists of positions should raise IndexError!
msg = "positional indexers are out-of-bounds"
with pytest.raises(IndexError, match=msg):
    df.iloc[:, [0, 1, 2, 3, 4, 5]]
with pytest.raises(IndexError, match=msg):
    df.iloc[[1, 30]]
with pytest.raises(IndexError, match=msg):
    df.iloc[[1, -30]]
with pytest.raises(IndexError, match=msg):
    df.iloc[[100]]

s = df["A"]
with pytest.raises(IndexError, match=msg):
    s.iloc[[100]]
with pytest.raises(IndexError, match=msg):
    s.iloc[[-100]]

# still raise on a single indexer
msg = "single positional indexer is out-of-bounds"
with pytest.raises(IndexError, match=msg):
    df.iloc[30]
with pytest.raises(IndexError, match=msg):
    df.iloc[-30]

# GH10779
# single positive/negative indexer exceeding Series bounds should raise
# an IndexError
with pytest.raises(IndexError, match=msg):
    s.iloc[30]
with pytest.raises(IndexError, match=msg):
    s.iloc[-30]

# slices are ok
result = df.iloc[:, 4:10]  # 0 < start < len < stop
expected = df.iloc[:, 4:]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, -4:-10]  # stop < 0 < start < len
expected = df.iloc[:, :0]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, 10:4:-1]  # 0 < stop < len < start (down)
expected = df.iloc[:, :4:-1]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, 4:-10:-1]  # stop < 0 < start < len (down)
expected = df.iloc[:, 4::-1]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, -10:4]  # start < 0 < stop < len
expected = df.iloc[:, :4]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, 10:4]  # 0 < stop < len < start
expected = df.iloc[:, :0]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, -10:-11:-1]  # stop < start < 0 < len (down)
expected = df.iloc[:, :0]
tm.assert_frame_equal(result, expected)

result = df.iloc[:, 10:11]  # 0 < len < start < stop
expected = df.iloc[:, :0]
tm.assert_frame_equal(result, expected)

# slice bounds exceeding is ok
result = s.iloc[18:30]
expected = s.iloc[18:]
tm.assert_series_equal(result, expected)

result = s.iloc[30:]
expected = s.iloc[:0]
tm.assert_series_equal(result, expected)

result = s.iloc[30::-1]
expected = s.iloc[::-1]
tm.assert_series_equal(result, expected)

# doc example
def check(result, expected):
    str(result)
    result.dtypes
    tm.assert_frame_equal(result, expected)

dfl = DataFrame(np.random.randn(5, 2), columns=list("AB"))
check(dfl.iloc[:, 2:3], DataFrame(index=dfl.index, columns=[]))
check(dfl.iloc[:, 1:3], dfl.iloc[:, [1]])
check(dfl.iloc[4:6], dfl.iloc[[4]])

msg = "positional indexers are out-of-bounds"
with pytest.raises(IndexError, match=msg):
    dfl.iloc[[4, 5, 6]]
msg = "single positional indexer is out-of-bounds"
with pytest.raises(IndexError, match=msg):
    dfl.iloc[:, 4]
