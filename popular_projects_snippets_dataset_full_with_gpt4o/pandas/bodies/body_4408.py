# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 26349
data = {"a": (i for i in (range(3))), "b": (i for i in reversed(range(3)))}
result = DataFrame(data)
expected = DataFrame({"a": [0, 1, 2], "b": [2, 1, 0]})
tm.assert_frame_equal(result, expected)
