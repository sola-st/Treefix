# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
empty = DataFrame()

result = empty.filter([])
tm.assert_frame_equal(result, empty)

result = empty.filter(like="foo")
tm.assert_frame_equal(result, empty)
