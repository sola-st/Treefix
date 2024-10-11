# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 7893
result = DataFrame(Series(1, name="foo"), columns=["bar"])
expected = DataFrame(columns=["bar"])
tm.assert_frame_equal(result, expected)
