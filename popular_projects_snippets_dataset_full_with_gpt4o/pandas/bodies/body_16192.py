# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
left = Series(np.random.randn(10))
right = Series(np.random.randn(10))

msg = "No axis named 1 for object type"
with pytest.raises(ValueError, match=msg):
    getattr(left, comparison_op.__name__)(right, axis=1)
