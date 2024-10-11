# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py
index = period_range(freq="A", start="1/1/2001", end="12/1/2009")
obj = DataFrame(np.random.randn(len(index), 5), index=index)

# invalid axis
with pytest.raises(ValueError, match="axis"):
    obj.to_timestamp(axis=2)
