# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# This test covers empty frame copying with non-empty column sets
# as reported in issue GH15370
empty_frame = DataFrame(data=[], index=[], columns=["A"])
empty_frame_copy = deepcopy(empty_frame)

tm.assert_frame_equal(empty_frame_copy, empty_frame)
