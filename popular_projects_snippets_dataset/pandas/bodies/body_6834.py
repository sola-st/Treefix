# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
"""breaks of length one produce an empty IntervalIndex"""
breaks = [0]
result = IntervalIndex.from_breaks(breaks)
expected = IntervalIndex.from_breaks([])
tm.assert_index_equal(result, expected)
