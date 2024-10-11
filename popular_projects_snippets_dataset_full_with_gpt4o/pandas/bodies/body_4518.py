# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

result = DataFrame({"A": [1.0, 2.0, None]}, dtype=string_dtype)
expected = DataFrame({"A": ["1.0", "2.0", None]}, dtype=object)
tm.assert_frame_equal(result, expected)
