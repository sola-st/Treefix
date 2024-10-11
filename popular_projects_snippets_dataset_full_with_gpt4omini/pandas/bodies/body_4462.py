# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 25691
result = DataFrame(tuples)
expected = DataFrame(lists)
tm.assert_frame_equal(result, expected)
