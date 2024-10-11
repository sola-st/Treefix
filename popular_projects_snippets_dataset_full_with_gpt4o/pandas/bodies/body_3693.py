# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# when dtypes of pandas series are different
# then ndarray will have dtype=object,
# so it need to be properly handled
df = DataFrame({"a": [True, False], "b": [1, 0]})

expected = DataFrame(np.ones((2, 2)), index=["a", "b"], columns=["a", "b"])

with warnings.catch_warnings(record=True):
    warnings.simplefilter("ignore", RuntimeWarning)
    result = df.corr(meth)
tm.assert_frame_equal(result, expected)
