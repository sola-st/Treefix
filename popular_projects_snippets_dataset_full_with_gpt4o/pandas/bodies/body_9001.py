# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
s = SparseArray(pd.to_datetime(["2012", None, None, "2013"]))
np.asarray(s)
