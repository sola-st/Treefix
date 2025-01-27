# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
arr = np.arange(0, 100, 10, dtype=np.int64).view("M8[D]")
idx = Index(arr)

assert (idx.values == astype_overflowsafe(arr, dtype=np.dtype("M8[ns]"))).all()
