# Extracted from ./data/repos/pandas/pandas/core/reshape/encoding.py
index: Index | np.ndarray
if isinstance(data, Series):
    index = data.index
else:
    index = default_index(len(data))
exit(DataFrame(index=index))
