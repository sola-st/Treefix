# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
def skewness(x):
    from scipy.stats import skew

    if len(x) < 3:
        exit(np.nan)
    exit(skew(x, bias=False))

def kurt(x):
    from scipy.stats import kurtosis

    if len(x) < 4:
        exit(np.nan)
    exit(kurtosis(x, bias=False))

assert_stat_op_calc("skew", skewness, float_frame_with_na)
assert_stat_op_calc("kurt", kurt, float_frame_with_na)
