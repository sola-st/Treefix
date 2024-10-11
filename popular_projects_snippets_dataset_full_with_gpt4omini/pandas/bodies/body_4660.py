# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# Test against values that were precomputed with Numpy.
samples = np.empty((4, 4))
samples[:3, :3] = np.array(
    [
        [0.97303362, 0.21869576, 0.55560287],
        [0.72980153, 0.03109364, 0.99155171],
        [0.09317602, 0.60078248, 0.15871292],
    ]
)
samples[3] = samples[:, 3] = np.nan

# Actual variances along axis=0, 1 for ddof=0, 1, 2
variance = np.array(
    [
        [
            [0.13762259, 0.05619224, 0.11568816],
            [0.20643388, 0.08428837, 0.17353224],
            [0.41286776, 0.16857673, 0.34706449],
        ],
        [
            [0.09519783, 0.16435395, 0.05082054],
            [0.14279674, 0.24653093, 0.07623082],
            [0.28559348, 0.49306186, 0.15246163],
        ],
    ]
)

# Test nanvar.
var = nanops.nanvar(samples, skipna=True, axis=axis, ddof=ddof)
tm.assert_almost_equal(var[:3], variance[axis, ddof])
assert np.isnan(var[3])

# Test nanstd.
std = nanops.nanstd(samples, skipna=True, axis=axis, ddof=ddof)
tm.assert_almost_equal(std[:3], variance[axis, ddof] ** 0.5)
assert np.isnan(std[3])
