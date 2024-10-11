# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#4576, GH#22880
# comparing DataFrame against list/tuple with len(obj) matching
#  len(df.columns) is supported as of GH#22800
df = DataFrame(np.arange(6).reshape((3, 2)))

expected = DataFrame([[False, False], [True, False], [False, False]])

result = df == (2, 2)
tm.assert_frame_equal(result, expected)

result = df == [2, 2]
tm.assert_frame_equal(result, expected)
