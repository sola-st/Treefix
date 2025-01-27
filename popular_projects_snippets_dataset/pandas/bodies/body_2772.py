# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Weight length must be right
msg = "Weights and axis to be sampled must be of same length"
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=[0, 1])

with pytest.raises(ValueError, match=msg):
    bad_weights = [0.5] * 11
    obj.sample(n=3, weights=bad_weights)

with pytest.raises(ValueError, match="Fewer non-zero entries in p than size"):
    bad_weight_series = Series([0, 0, 0.2])
    obj.sample(n=4, weights=bad_weight_series)
