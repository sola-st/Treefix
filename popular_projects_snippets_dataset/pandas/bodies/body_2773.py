# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Check won't accept negative weights
bad_weights = [-0.1] * 10
msg = "weight vector many not include negative values"
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=bad_weights)
