# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
ser = pd.Series(data)
mask = np.zeros(len(data), dtype=bool)
mask[:2] = True

if as_callable:
    mask2 = lambda x: mask
else:
    mask2 = mask

if setter:
    # loc
    target = getattr(ser, setter)
else:
    # Series.__setitem__
    target = ser

target[mask2] = data[5:7]

ser[mask2] = data[5:7]
assert ser[0] == data[5]
assert ser[1] == data[6]
