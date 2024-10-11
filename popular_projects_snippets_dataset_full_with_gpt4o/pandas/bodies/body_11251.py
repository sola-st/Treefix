# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 17537
frame = mframe
deleveled = frame.reset_index()

result0 = frame.groupby(level=0, sort=sort).sum()
result1 = frame.groupby(level=1, sort=sort).sum()

expected0 = frame.groupby(deleveled["first"].values, sort=sort).sum()
expected1 = frame.groupby(deleveled["second"].values, sort=sort).sum()

expected0.index.name = "first"
expected1.index.name = "second"

assert result0.index.name == "first"
assert result1.index.name == "second"

tm.assert_frame_equal(result0, expected0)
tm.assert_frame_equal(result1, expected1)
assert result0.index.name == frame.index.names[0]
assert result1.index.name == frame.index.names[1]

# groupby level name
result0 = frame.groupby(level="first", sort=sort).sum()
result1 = frame.groupby(level="second", sort=sort).sum()
tm.assert_frame_equal(result0, expected0)
tm.assert_frame_equal(result1, expected1)

# axis=1

result0 = frame.T.groupby(level=0, axis=1, sort=sort).sum()
result1 = frame.T.groupby(level=1, axis=1, sort=sort).sum()
tm.assert_frame_equal(result0, expected0.T)
tm.assert_frame_equal(result1, expected1.T)

# raise exception for non-MultiIndex
msg = "level > 0 or level < -1 only valid with MultiIndex"
with pytest.raises(ValueError, match=msg):
    df.groupby(level=1)
