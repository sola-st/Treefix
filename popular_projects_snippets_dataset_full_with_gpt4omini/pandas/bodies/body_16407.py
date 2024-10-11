# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
msg = "Input must be a list-like of list-likes"

with pytest.raises(TypeError, match=msg):
    cartesian_product(X=X)
