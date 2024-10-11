# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pipe.py
obj = DataFrame({"A": [1, 2, 3]})
expected = DataFrame({"A": [1, 4, 9]})
if frame_or_series is Series:
    obj = obj["A"]
    expected = expected["A"]

f = lambda x, y: x**y
result = obj.pipe(f, 2)
tm.assert_equal(result, expected)
