# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH3659
# non-unique indexer with loc slice
# https://groups.google.com/forum/?fromgroups#!topic/pydata/zTm2No0crYs

# these are going to raise because the we are non monotonic
df = DataFrame(
    {"A": [1, 2, 3, 4, 5, 6], "B": [3, 4, 5, 6, 7, 8]}, index=[0, 1, 0, 1, 2, 3]
)
msg = "'Cannot get left slice bound for non-unique label: 1'"
with pytest.raises(KeyError, match=msg):
    df.loc[1:]
msg = "'Cannot get left slice bound for non-unique label: 0'"
with pytest.raises(KeyError, match=msg):
    df.loc[0:]
msg = "'Cannot get left slice bound for non-unique label: 1'"
with pytest.raises(KeyError, match=msg):
    df.loc[1:2]

# monotonic are ok
df = DataFrame(
    {"A": [1, 2, 3, 4, 5, 6], "B": [3, 4, 5, 6, 7, 8]}, index=[0, 1, 0, 1, 2, 3]
).sort_index(axis=0)
result = df.loc[1:]
expected = DataFrame({"A": [2, 4, 5, 6], "B": [4, 6, 7, 8]}, index=[1, 1, 2, 3])
tm.assert_frame_equal(result, expected)

result = df.loc[0:]
tm.assert_frame_equal(result, df)

result = df.loc[1:2]
expected = DataFrame({"A": [2, 4, 5], "B": [4, 6, 7]}, index=[1, 1, 2])
tm.assert_frame_equal(result, expected)
