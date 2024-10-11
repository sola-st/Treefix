# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
# shape: [batch=2, n_bins=3]
histograms = [[0.2, 0.1, 0.7],
              [0.3, 0.45, 0.25]]

# shape: [batch=3, batch=2]
devent = [
    [0, 0],
    [1, 1],
    [2, 2]
]
dist = categorical.Categorical(probs=histograms)

# We test that the probabilities are correctly broadcasted over the
# additional leading batch dimension of size 3.
expected_cdf_result = np.zeros((3, 2))
expected_cdf_result[0, 0] = 0
expected_cdf_result[0, 1] = 0
expected_cdf_result[1, 0] = 0.2
expected_cdf_result[1, 1] = 0.3
expected_cdf_result[2, 0] = 0.3
expected_cdf_result[2, 1] = 0.75

with self.cached_session():
    self.assertAllClose(dist.cdf(devent), expected_cdf_result)
