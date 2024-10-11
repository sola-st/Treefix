# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 20624
actual = DataFrame(DataFrame(), dtype="object")
expected = DataFrame([], dtype="object")
tm.assert_frame_equal(actual, expected)
