# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
msg = "matrices are not aligned"
with pytest.raises(ValueError, match=msg):
    obj.dot(other.T)
