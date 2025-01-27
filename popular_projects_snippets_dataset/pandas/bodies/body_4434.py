# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#43986
ser = Series([1, 2])

arr = np.array([None, None], dtype=object)
arr[0] = ser
arr[1] = ser * 2

df = DataFrame(arr)
expected = DataFrame(pd.array(arr))
tm.assert_frame_equal(df, expected)
assert df.shape == (2, 1)
tm.assert_numpy_array_equal(df[0].values, arr)
