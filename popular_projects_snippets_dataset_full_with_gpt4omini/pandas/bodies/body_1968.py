# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_time.py
arg = ["14:15", "20:20"]
expected_arr = [time(14, 15), time(20, 20)]
assert to_time(arg) == expected_arr
assert to_time(arg, format="%H:%M") == expected_arr
assert to_time(arg, infer_time_format=True) == expected_arr
assert to_time(arg, format="%I:%M%p", errors="coerce") == [None, None]

res = to_time(arg, format="%I:%M%p", errors="ignore")
tm.assert_numpy_array_equal(res, np.array(arg, dtype=np.object_))

msg = "Cannot convert.+to a time with given format"
with pytest.raises(ValueError, match=msg):
    to_time(arg, format="%I:%M%p", errors="raise")

tm.assert_series_equal(
    to_time(Series(arg, name="test")), Series(expected_arr, name="test")
)

res = to_time(np.array(arg))
assert isinstance(res, list)
assert res == expected_arr
