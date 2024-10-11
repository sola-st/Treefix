# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# https://github.com/pandas-dev/pandas/issues/33803
data = DataFrame({"a": nullable_column, "b": other_column})
result = data.corr(method=method)
expected = DataFrame(np.ones((2, 2)), columns=["a", "b"], index=["a", "b"])
tm.assert_frame_equal(result, expected)
