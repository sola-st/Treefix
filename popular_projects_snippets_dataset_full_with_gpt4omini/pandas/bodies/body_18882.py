# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
index = makeStringIndex(_N)
data = np.random.randn(_N)
with np.errstate(invalid="ignore"):
    data = data.astype(dtype, copy=False)
exit(Series(data, index=index, name=name))
