# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 22051
df = DataFrame({"a": data})
df_copy = df.where(pd.notnull(df), None).copy()
df.where(pd.notnull(df), None, inplace=True)
tm.assert_equal(df, df_copy)
