# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
SLC = pd.IndexSlice

idx = Index(idx)
ser = Series(np.arange(20), index=idx)
tm.assert_indexing_slices_equivalent(ser, SLC[idx[9] :: -1], SLC[9::-1])
tm.assert_indexing_slices_equivalent(ser, SLC[: idx[9] : -1], SLC[:8:-1])
tm.assert_indexing_slices_equivalent(
    ser, SLC[idx[13] : idx[9] : -1], SLC[13:8:-1]
)
tm.assert_indexing_slices_equivalent(ser, SLC[idx[9] : idx[13] : -1], SLC[:0])
