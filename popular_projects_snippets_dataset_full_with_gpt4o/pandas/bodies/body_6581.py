# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
index = Index(list("bcdxy"))

s_start, s_stop = index.slice_locs(in_slice.start, in_slice.stop, in_slice.step)
result = index[s_start : s_stop : in_slice.step]
expected = Index(list(expected))
tm.assert_index_equal(result, expected)
