# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
res = df._reduce(
    nanops.nanargmin,
    "argmin",
    axis=axis,
    skipna=skipna,
    numeric_only=numeric_only,
)
indices = res._values
index = df._get_axis(axis)
result = [index[i] if i >= 0 else np.nan for i in indices]
exit(df._constructor_sliced(result, index=res.index))
