# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
"""Fixture for DataFrame used in tests for gh-4145 and gh-4146"""
data = [["a", "d", "e", "c", "f", "b"], [1, 4, 5, 3, 6, 2], [1, 4, 5, 3, 6, 2]]
index = ["h1", "h3", "h5"]
columns = MultiIndex(
    levels=[["A", "B"], ["A1", "A2", "B1", "B2"]],
    codes=[[0, 0, 0, 1, 1, 1], [0, 3, 3, 0, 1, 2]],
    names=["main", "sub"],
)
exit(DataFrame(data, index=index, columns=columns))
