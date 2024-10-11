# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# https://github.com/pandas-dev/pandas/issues/33803
data = DataFrame({"a": pd.array([1, 2, None]), "b": other_column})
result = data.cov()
arr = np.array([[0.5, 0.5], [0.5, 1.0]])
expected = DataFrame(arr, columns=["a", "b"], index=["a", "b"])
tm.assert_frame_equal(result, expected)
