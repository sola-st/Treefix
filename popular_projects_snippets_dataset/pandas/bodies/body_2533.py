# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# Check that non-nano dt64 values get cast to dt64 on setitem
#  into a not-yet-existing column
n = 100

dtype = np.dtype(f"M8[{unit}]")
vals = np.arange(n, dtype=np.int64).view(dtype)
if unit in ["s", "ms"]:
    # supported unit
    ex_vals = vals
else:
    # we get the nearest supported units, i.e. "s"
    ex_vals = vals.astype("datetime64[s]")

df = DataFrame({"ints": np.arange(n)}, index=np.arange(n))
df[unit] = vals

assert df[unit].dtype == ex_vals.dtype
assert (df[unit].values == ex_vals).all()
