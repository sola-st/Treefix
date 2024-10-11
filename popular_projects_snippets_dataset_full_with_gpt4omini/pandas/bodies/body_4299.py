# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#28600
df = DataFrame(columns=["A", "B"], dtype=np.float64)
ser = Series([1, 2], index=["A", "B"])

result = df + ser
expected = df
tm.assert_frame_equal(result, expected)
