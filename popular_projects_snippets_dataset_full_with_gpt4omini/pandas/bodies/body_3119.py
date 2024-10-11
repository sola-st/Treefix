# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#44978 periods > len(columns)
df = DataFrame(np.random.rand(5, 3))
shifted = df.shift(6, axis=1, fill_value=None)

expected = df * np.nan
tm.assert_frame_equal(shifted, expected)

shifted2 = df.shift(-6, axis=1, fill_value=None)
tm.assert_frame_equal(shifted2, expected)
