# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# GH#41320
df = DataFrame(
    {0: [1, 3, 5, 7], 1: [2, 4, 6, 8], 2: [1.5, 3.5, 5.5, 7.5]},
    index=["a", "a", "b", "b"],
)
gb = df.groupby(level=0, axis=0)

res = gb.rank(axis=1)

# This should match what we get when "manually" operating group-by-group
expected = concat([df.loc["a"].rank(axis=1), df.loc["b"].rank(axis=1)], axis=0)
tm.assert_frame_equal(res, expected)

# check that we haven't accidentally written a case that coincidentally
# matches rank(axis=0)
alt = gb.rank(axis=0)
assert not alt.equals(expected)
