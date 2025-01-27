# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
msg = "operands could not be broadcast together"
with pytest.raises(ValueError, match=msg):
    idx * idx[0:3]
with pytest.raises(ValueError, match=msg):
    idx * np.array([1, 2])
