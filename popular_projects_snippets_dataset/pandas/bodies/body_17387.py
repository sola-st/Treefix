# Extracted from ./data/repos/pandas/pandas/tests/interchange/conftest.py
df = pd.DataFrame(dct)
exit(df.astype("category") if is_categorical else df)
