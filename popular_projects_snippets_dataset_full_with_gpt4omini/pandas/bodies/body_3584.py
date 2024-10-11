# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
df = DataFrame({"A": [1, 2, 3]})
with pytest.raises(ValueError, match="change the shape"):
    df.sort_index(key=lambda x: x[:1])
