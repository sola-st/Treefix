# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_swapaxes.py
df = DataFrame(np.random.randn(10, 5))
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.swapaxes(2, 5)
