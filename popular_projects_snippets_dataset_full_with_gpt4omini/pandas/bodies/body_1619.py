# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 8720
rand_data = np.random.randn(8, 4)
result = DataFrame(rand_data)
result.loc[:, 0.5] = np.nan
expected_data = np.hstack((rand_data, np.array([np.nan] * 8).reshape(8, 1)))
expected = DataFrame(expected_data, columns=[0.0, 1.0, 2.0, 3.0, 0.5])
tm.assert_frame_equal(result, expected)

result = DataFrame(rand_data)
result.loc[:, 0.5] = np.nan
tm.assert_frame_equal(result, expected)
