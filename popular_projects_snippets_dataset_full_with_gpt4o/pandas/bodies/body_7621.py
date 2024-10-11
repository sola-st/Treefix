# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# MI with a NaT
mi = MultiIndex(
    levels=[["C"], date_range("2012-01-01", periods=5)],
    codes=[[0, 0, 0, 0, 0, 0], [-1, 0, 1, 2, 3, 4]],
    names=[None, "B"],
)
assert ("C", pd.Timestamp("2012-01-01")) in mi
for val in mi.values:
    assert val in mi
