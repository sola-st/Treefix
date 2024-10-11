# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 25753
df = DataFrame(
    np.random.randn(len(index), len(columns)), index=index, columns=columns
)
msg = ".iloc requires numeric indexers, got"
with pytest.raises(IndexError, match=msg):
    df.iloc[index_vals, column_vals]
