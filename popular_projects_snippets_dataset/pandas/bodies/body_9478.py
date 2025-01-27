# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
msg = r"Either `left` or `right` need to be a np\.ndarray."
with pytest.raises(TypeError, match=msg):
    # masks need to be non-None, otherwise it ends up in an infinite recursion
    operation(True, True, np.zeros(1), np.zeros(1))
