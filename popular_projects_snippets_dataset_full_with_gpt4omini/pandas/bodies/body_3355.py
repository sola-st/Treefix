# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH-44499
nullable_ser = Series([1, 0, 1], dtype=dtype)
df = DataFrame({"A": ["A", "B", "x"], "B": nullable_ser})
result = df.replace("x", "X")
expected = DataFrame({"A": ["A", "B", "X"], "B": nullable_ser})
tm.assert_frame_equal(result, expected)
