# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
exp_df = DataFrame({"A": expected, "B": expected})

if axis == 1:
    df = df.T
    exp_df = exp_df.T

result = df.rank(method=method, axis=axis)
tm.assert_frame_equal(result, exp_df)
