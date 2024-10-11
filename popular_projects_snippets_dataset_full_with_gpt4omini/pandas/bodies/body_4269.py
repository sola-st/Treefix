# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# one instance of parametrized fixture
op = all_arithmetic_operators

# Check that arrays with dim >= 3 raise
arr = np.ones((1,) * dim)
msg = "Unable to coerce to Series/DataFrame"
with pytest.raises(ValueError, match=msg):
    getattr(float_frame, op)(arr)
