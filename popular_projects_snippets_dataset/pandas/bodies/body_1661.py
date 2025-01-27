# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
df = df.sort_values(df.columns.tolist())
df.index = np.arange(len(df))
exit(df)
