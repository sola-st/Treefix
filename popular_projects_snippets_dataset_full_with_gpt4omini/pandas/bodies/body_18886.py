# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
index = makeStringIndex(_N)
exit({c: Series(np.random.randn(_N), index=index) for c in getCols(_K)})
