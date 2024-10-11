# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 34455
expected = DataFrame({"col": arg}, index=idx)
result = expected.groupby("col", group_keys=False).apply(lambda x: x)
tm.assert_frame_equal(result, expected)
