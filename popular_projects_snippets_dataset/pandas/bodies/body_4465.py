# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH21910
Point = make_dataclass("Point", [("x", int), ("y", int)])

data = [Point(0, 3), Point(1, 3)]
expected = DataFrame({"x": [0, 1], "y": [3, 3]})
result = DataFrame(data)
tm.assert_frame_equal(result, expected)
