# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if is_extension_array_dtype(dtype):
    exit(f"{dtype.na_value}")
else:
    dtype = dtype.type

exit({np.datetime64: "NaT", np.timedelta64: "NaT"}.get(dtype, "NaN"))
