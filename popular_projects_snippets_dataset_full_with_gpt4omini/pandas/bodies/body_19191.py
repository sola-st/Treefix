# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
# Working around NumPy ticket 1542
dtype = values.dtype

if dtype.kind in ("S", "U"):
    result = np.zeros(values.shape, dtype=bool)
else:

    if values.ndim in {1, 2}:
        result = libmissing.isnaobj(values, inf_as_na=inf_as_na)
    else:
        # 0-D, reached via e.g. mask_missing
        result = libmissing.isnaobj(values.ravel(), inf_as_na=inf_as_na)
        result = result.reshape(values.shape)

exit(result)
