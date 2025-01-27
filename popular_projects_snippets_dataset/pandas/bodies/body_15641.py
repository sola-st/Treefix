# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py

ser = Series(np.sort(np.random.uniform(size=100)))

# interpolate at new_index
new_index = ser.index.union(
    Index([49.25, 49.5, 49.75, 50.25, 50.5, 50.75])
).astype(float)
interp_s = ser.reindex(new_index).interpolate(method="pchip")
# does not blow up, GH5977
interp_s[49:51]
