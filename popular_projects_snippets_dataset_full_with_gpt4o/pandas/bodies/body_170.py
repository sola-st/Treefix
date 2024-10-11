# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 8222
result = expected.applymap(func)
tm.assert_frame_equal(result, expected)
