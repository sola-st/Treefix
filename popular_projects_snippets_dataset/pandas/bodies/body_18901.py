# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
df = makeDataFrame()
i, j = _create_missing_idx(*df.shape, density=density, random_state=random_state)
df.values[i, j] = np.nan
exit(df)
