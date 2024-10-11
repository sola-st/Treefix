# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# All missing weights

nan_weights = [np.nan] * 10
with pytest.raises(ValueError, match="Invalid weights: weights sum to zero"):
    obj.sample(n=3, weights=nan_weights)
