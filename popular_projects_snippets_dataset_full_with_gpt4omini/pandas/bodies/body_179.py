# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 21063
df = DataFrame([[0, 1], [2, 3]], columns=["a", "a"])
expected = DataFrame([[0, 1]], columns=["a", "a"], index=["min"])
result = df.agg(["min"])

tm.assert_frame_equal(result, expected)
