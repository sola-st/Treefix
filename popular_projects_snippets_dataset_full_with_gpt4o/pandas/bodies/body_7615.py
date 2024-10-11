# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#30053
idx = MultiIndex(
    levels=[["a"], [0, 7], [1]],
    codes=[[0, 0], [1, 0], [0, 0]],
    names=["x", "y", "z"],
    sortorder=0,
)
key = ("a", 7)

with tm.assert_produces_warning(PerformanceWarning):
    # PerformanceWarning: indexing past lexsort depth may impact performance
    result = idx.get_loc(key)

assert result == slice(0, 1, None)
