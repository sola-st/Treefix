# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
result = datetime_frame.sem(ddof=4)
expected = datetime_frame.apply(lambda x: x.std(ddof=4) / np.sqrt(len(x)))
tm.assert_almost_equal(result, expected)

arr = np.repeat(np.random.random((1, 1000)), 1000, 0)
result = nanops.nansem(arr, axis=0)
assert not (result < 0).any()

with pd.option_context("use_bottleneck", False):
    result = nanops.nansem(arr, axis=0)
    assert not (result < 0).any()
