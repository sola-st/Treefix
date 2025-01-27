# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_equivalence.py
# make sure take is not using -1
i = MultiIndex.from_tuples([(0, pd.NaT), (0, pd.Timestamp("20130101"))])
result = i[0:1].equals(i[0])
assert not result
result = i[1:2].equals(i[1])
assert not result
