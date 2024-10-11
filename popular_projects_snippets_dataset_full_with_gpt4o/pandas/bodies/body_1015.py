# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py
ser = Series(
    np.arange(20), MultiIndex.from_product([list("abcde"), np.arange(4)])
)
SLC = pd.IndexSlice

tm.assert_indexing_slices_equivalent(ser, SLC[::-1], SLC[::-1])

tm.assert_indexing_slices_equivalent(ser, SLC["d"::-1], SLC[15::-1])
tm.assert_indexing_slices_equivalent(ser, SLC[("d",)::-1], SLC[15::-1])

tm.assert_indexing_slices_equivalent(ser, SLC[:"d":-1], SLC[:11:-1])
tm.assert_indexing_slices_equivalent(ser, SLC[:("d",):-1], SLC[:11:-1])

tm.assert_indexing_slices_equivalent(ser, SLC["d":"b":-1], SLC[15:3:-1])
tm.assert_indexing_slices_equivalent(ser, SLC[("d",):"b":-1], SLC[15:3:-1])
tm.assert_indexing_slices_equivalent(ser, SLC["d":("b",):-1], SLC[15:3:-1])
tm.assert_indexing_slices_equivalent(ser, SLC[("d",):("b",):-1], SLC[15:3:-1])
tm.assert_indexing_slices_equivalent(ser, SLC["b":"d":-1], SLC[:0])

tm.assert_indexing_slices_equivalent(ser, SLC[("c", 2)::-1], SLC[10::-1])
tm.assert_indexing_slices_equivalent(ser, SLC[:("c", 2):-1], SLC[:9:-1])
tm.assert_indexing_slices_equivalent(
    ser, SLC[("e", 0):("c", 2):-1], SLC[16:9:-1]
)
