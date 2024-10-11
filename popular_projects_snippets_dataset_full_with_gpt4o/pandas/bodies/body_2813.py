# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
smaller = int_frame.reindex(int_frame.index[::2])

assert smaller["A"].dtype == np.int64

bigger = smaller.reindex(int_frame.index)
assert bigger["A"].dtype == np.float64

smaller = int_frame.reindex(columns=["A", "B"])
assert smaller["A"].dtype == np.int64
