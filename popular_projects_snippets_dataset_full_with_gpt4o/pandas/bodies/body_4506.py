# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
expected = DataFrame({"A": [0, 1, 2, 3, 4]}, dtype=dtype or "int64")

# GH 26342
result = DataFrame(range(5), columns=["A"], dtype=dtype)
tm.assert_frame_equal(result, expected)

# GH 16804
result = DataFrame({"A": range(5)}, dtype=dtype)
tm.assert_frame_equal(result, expected)
