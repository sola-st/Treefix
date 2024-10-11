# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# https://github.com/pandas-dev/pandas/issues/37174
arr = np.array([1, 2, 3])
arr.setflags(write=False)
df = DataFrame([1, 2, 3])
result = df.isin(arr)
expected = DataFrame([True, True, True])
tm.assert_frame_equal(result, expected)
