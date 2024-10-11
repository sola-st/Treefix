# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 2476
expected = DataFrame(index=["a"])
result = expected.apply(lambda x: x["a"], axis=1)
tm.assert_frame_equal(result, expected)
