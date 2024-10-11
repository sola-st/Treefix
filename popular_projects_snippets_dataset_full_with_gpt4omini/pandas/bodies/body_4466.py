# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH21910
# varying types
Point = make_dataclass("Point", [("x", int), ("y", int)])
HLine = make_dataclass("HLine", [("x0", int), ("x1", int), ("y", int)])

data = [Point(0, 3), HLine(1, 3, 3)]

expected = DataFrame(
    {"x": [0, np.nan], "y": [3, 3], "x0": [np.nan, 1], "x1": [np.nan, 3]}
)
result = DataFrame(data)
tm.assert_frame_equal(result, expected)
