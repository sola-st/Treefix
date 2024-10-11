# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
tuples = [(1, 2, None, 3), (1, 2, None, 3), (None, 2, 5, 3)]

df = DataFrame.from_records(tuples, columns=["a", "b", "c", "d"])
assert np.isnan(df["c"][0])
