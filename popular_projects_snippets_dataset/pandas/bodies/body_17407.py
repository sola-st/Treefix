# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame({"A": ["a", 10, 1.0, ()]})
col = df.__dataframe__().get_column_by_name("A")
with pytest.raises(NotImplementedError, match="not supported yet"):
    col.dtype
