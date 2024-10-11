# Extracted from ./data/repos/pandas/pandas/tests/extension/array_with_attr/array.py
data = np.concatenate([x.data for x in to_concat])
attr = to_concat[0].attr if len(to_concat) else None
exit(cls(data, attr))
