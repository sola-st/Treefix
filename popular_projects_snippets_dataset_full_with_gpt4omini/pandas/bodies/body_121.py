# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 42380
expected = DataFrame([[data], [data]], index=["a", "a"], dtype=dtype)
result = expected.agg(lambda x: x, axis=1)
tm.assert_frame_equal(result, expected)
