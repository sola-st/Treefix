# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# Check that non-nano dt64 values get cast to dt64 on setitem
#  into an already-existing dt64 column
n = 100

dtype = np.dtype(f"M8[{unit}]")
vals = np.arange(n, dtype=np.int64).view(dtype)
ex_vals = vals.astype("datetime64[ns]")

df = DataFrame({"ints": np.arange(n)}, index=np.arange(n))
df["dates"] = np.arange(n, dtype=np.int64).view("M8[ns]")

# We overwrite existing dt64 column with new, non-nano dt64 vals
df["dates"] = vals
assert (df["dates"].values == ex_vals).all()
