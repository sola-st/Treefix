# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
df = DataFrame(np.random.randn(2, 2))
with pytest.raises(ValueError, match="periods must be an integer"):
    df.diff(1.5)
