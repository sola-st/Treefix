# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
ser = pd.Series(data)
mask = np.zeros(len(data), dtype=bool)
mask[:2] = True

if setter:  # loc
    target = getattr(ser, setter)
else:  # __setitem__
    target = ser

target[mask] = data[10]
assert ser[0] == data[10]
assert ser[1] == data[10]
