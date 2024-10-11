# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
result = tsframe.groupby(lambda x: x.year, group_keys=False).apply(lambda x: x * 2)
expected = tsframe * 2
tm.assert_frame_equal(result, expected)
