# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# All zeros raises errors

zero_weights = [0] * 10
with pytest.raises(ValueError, match="Invalid weights: weights sum to zero"):
    obj.sample(n=3, weights=zero_weights)
