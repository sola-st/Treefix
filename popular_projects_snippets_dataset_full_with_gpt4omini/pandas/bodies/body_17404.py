# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame(data)
df2 = df.__dataframe__()

for col_name in df.columns:
    assert df2.get_column_by_name(col_name).null_count == 0
