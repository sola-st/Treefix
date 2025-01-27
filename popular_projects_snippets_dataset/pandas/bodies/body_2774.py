# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Check inf and -inf throw errors:

weights_with_inf = [0.1] * 10
weights_with_inf[0] = np.inf
msg = "weight vector may not include `inf` values"
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=weights_with_inf)

weights_with_ninf = [0.1] * 10
weights_with_ninf[0] = -np.inf
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, weights=weights_with_ninf)
