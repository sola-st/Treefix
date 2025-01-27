# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# https://github.com/pandas-dev/pandas/issues/35460
df = DataFrame(columns=["a"]).astype(dtype_str)

other = DataFrame({"a": [np.timedelta64(val, "ns")]})
result = df._append(other, ignore_index=True)

expected = other.astype(object)
tm.assert_frame_equal(result, expected)
