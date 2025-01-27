# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
data = {"A": np.random.randn(10), "B": np.random.randn(8)}
with pytest.raises(ValueError, match="All arrays must be of the same length"):
    DataFrame(data)
