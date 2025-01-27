# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
df = pd.DataFrame({"A": [0, 1]})
with pytest.raises(AttributeError, match="sparse"):
    df.sparse
