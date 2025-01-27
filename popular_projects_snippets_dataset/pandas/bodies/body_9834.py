# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# see gh-26055
df = DataFrame({"x": range(3), "y": range(3)})

axis = df._get_axis_number(axis_frame)

if axis in [0, "index"]:
    expected = DataFrame({"x": [1.0, 2.0, 2.0], "y": [1.0, 2.0, 2.0]})
else:
    expected = DataFrame({"x": [1.0, 1.0, 1.0], "y": [2.0, 2.0, 2.0]})

result = df.rolling(2, axis=axis_frame, min_periods=0).count()
tm.assert_frame_equal(result, expected)
