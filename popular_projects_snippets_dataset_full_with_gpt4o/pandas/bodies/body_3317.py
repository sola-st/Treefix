# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
df = self.df

def _check2d(df, expected, method="average", axis=0):
    exp_df = DataFrame({"A": expected, "B": expected})

    if axis == 1:
        df = df.T
        exp_df = exp_df.T

    result = df.rank(method=method, axis=axis)
    tm.assert_frame_equal(result, exp_df)

frame = df if dtype is None else df.astype(dtype)
_check2d(frame, self.results[method], method=method, axis=axis)
