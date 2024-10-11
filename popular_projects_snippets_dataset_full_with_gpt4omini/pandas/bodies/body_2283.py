# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_mask.py
# GH 40824
obj = DataFrame(
    {"A": ["foo", "bar", "baz", NA]},
    index=["id1", "id2", "id3", "id4"],
    dtype=StringDtype(),
)
filtered_obj = DataFrame(
    {"A": ["this", "that"]}, index=["id2", "id3"], dtype=StringDtype()
)
expected = DataFrame(
    {"A": [NA, "this", "that", NA]},
    index=["id1", "id2", "id3", "id4"],
    dtype=StringDtype(),
)
if frame_or_series is Series:
    obj = obj["A"]
    filtered_obj = filtered_obj["A"]
    expected = expected["A"]

filter_ser = Series([False, True, True, False])
result = obj.mask(filter_ser, filtered_obj)

tm.assert_equal(result, expected)
