# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
target, source = target_source
expected = target.join(source, on="C")
del expected["C"]

join_col = target.pop("C")
result = target.join(source, on=join_col)
tm.assert_frame_equal(result, expected)
