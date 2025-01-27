# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH40824
obj = frame_or_series(
    ["a", "b", "c", "d"], index=["id1", "id2", "id3", "id4"], dtype=StringDtype()
)
filtered_obj = frame_or_series(
    ["b", "c"], index=["id2", "id3"], dtype=StringDtype()
)
filter_ser = Series([False, True, True, False])

result = obj.where(filter_ser, filtered_obj)
expected = frame_or_series(
    [pd.NA, "b", "c", pd.NA],
    index=["id1", "id2", "id3", "id4"],
    dtype=StringDtype(),
)
tm.assert_equal(result, expected)

result = obj.mask(~filter_ser, filtered_obj)
tm.assert_equal(result, expected)

obj.mask(~filter_ser, filtered_obj, inplace=True)
tm.assert_equal(result, expected)
