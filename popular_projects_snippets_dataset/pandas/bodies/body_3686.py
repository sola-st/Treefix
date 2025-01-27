# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#34611
np_array1 = np.random.rand(10)
np_array2 = np.random.rand(10)
df = DataFrame({0: np_array1, 1: np_array2})
result = df.cov(ddof=test_ddof)
expected_np = np.cov(np_array1, np_array2, ddof=test_ddof)
expected = DataFrame(expected_np)
tm.assert_frame_equal(result, expected)
