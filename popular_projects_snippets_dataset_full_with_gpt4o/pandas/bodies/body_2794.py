# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/29896
# tests for reindexing a multi-indexed DataFrame with a new MultiIndex
#
# confirms that we can reindex a multi-indexed DataFrame with a new
# MultiIndex object correctly when using no filling, backfilling, and
# padding
#
# The DataFrame, `df`, used in this test is:
#       c
#  a b
# -1 0  A
#    1  B
#    2  C
#    3  D
#    4  E
#    5  F
#    6  G
#  0 0  A
#    1  B
#    2  C
#    3  D
#    4  E
#    5  F
#    6  G
#  1 0  A
#    1  B
#    2  C
#    3  D
#    4  E
#    5  F
#    6  G
#
# and the other MultiIndex, `new_multi_index`, is:
# 0: 0 0.5
# 1:   2.0
# 2:   5.0
# 3:   5.8
df = DataFrame(
    {
        "a": [-1] * 7 + [0] * 7 + [1] * 7,
        "b": list(range(7)) * 3,
        "c": ["A", "B", "C", "D", "E", "F", "G"] * 3,
    }
).set_index(["a", "b"])
new_index = [0.5, 2.0, 5.0, 5.8]
new_multi_index = MultiIndex.from_product([[0], new_index], names=["a", "b"])

# reindexing w/o a `method` value
reindexed = df.reindex(new_multi_index)
expected = DataFrame(
    {"a": [0] * 4, "b": new_index, "c": [np.nan, "C", "F", np.nan]}
).set_index(["a", "b"])
tm.assert_frame_equal(expected, reindexed)

# reindexing with backfilling
expected = DataFrame(
    {"a": [0] * 4, "b": new_index, "c": ["B", "C", "F", "G"]}
).set_index(["a", "b"])
reindexed_with_backfilling = df.reindex(new_multi_index, method="bfill")
tm.assert_frame_equal(expected, reindexed_with_backfilling)

reindexed_with_backfilling = df.reindex(new_multi_index, method="backfill")
tm.assert_frame_equal(expected, reindexed_with_backfilling)

# reindexing with padding
expected = DataFrame(
    {"a": [0] * 4, "b": new_index, "c": ["A", "C", "F", "F"]}
).set_index(["a", "b"])
reindexed_with_padding = df.reindex(new_multi_index, method="pad")
tm.assert_frame_equal(expected, reindexed_with_padding)

reindexed_with_padding = df.reindex(new_multi_index, method="ffill")
tm.assert_frame_equal(expected, reindexed_with_padding)
