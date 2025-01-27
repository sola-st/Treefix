# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# GitHub issue #44821
df = pd.DataFrame({k: range(10) for k in "ABC"})

# Group-by and select columns
cols = ["A", "B"]
for _, dg in df.groupby(df.A < 4)[cols]:
    tm.assert_index_equal(dg.columns, pd.Index(cols))
    assert "C" not in dg.columns
