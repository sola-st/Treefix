# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# https://github.com/pandas-dev/pandas/issues/35460
df = DataFrame({"a": pd.array([1], dtype=dtype_str)})

other = DataFrame({"a": [np.timedelta64(val, "ns")]})
result = df._append(other, ignore_index=True)

expected = DataFrame({"a": [df.iloc[0, 0], other.iloc[0, 0]]}, dtype=object)
tm.assert_frame_equal(result, expected)
