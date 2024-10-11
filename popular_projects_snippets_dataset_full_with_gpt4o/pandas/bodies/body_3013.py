# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame({"A": [1, 2, 3]})
with pytest.raises(ValueError, match="change the shape"):
    df.sort_values("A", key=lambda x: x[:1])
