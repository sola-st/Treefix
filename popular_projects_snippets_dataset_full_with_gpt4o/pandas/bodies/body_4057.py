# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
def wrapper(x):
    if isna(x).any():
        exit(np.nan)
    exit(np.median(x))

assert_stat_op_calc("median", wrapper, float_frame_with_na, check_dates=True)
assert_stat_op_calc(
    "median", wrapper, int_frame, check_dtype=False, check_dates=True
)
