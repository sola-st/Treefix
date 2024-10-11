# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# map test on StringDType, GH#40823
ser1 = Series(
    data=["cat", "dog", "rabbit"],
    index=["id1", "id2", "id3"],
    dtype=any_string_dtype,
)
ser2 = Series(data=["id3", "id2", "id1", "id7000"], dtype=any_string_dtype)
result = ser2.map(ser1)
expected = Series(data=["rabbit", "dog", "cat", pd.NA], dtype=any_string_dtype)

tm.assert_series_equal(result, expected)
