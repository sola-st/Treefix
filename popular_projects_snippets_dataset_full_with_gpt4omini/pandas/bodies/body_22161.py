# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if is_object_dtype(vals.dtype) and skipna:
    # GH#37501: don't raise on pd.NA when skipna=True
    mask = isna(vals)
    if mask.any():
        # mask on original values computed separately
        vals = vals.copy()
        vals[mask] = True
elif isinstance(vals, BaseMaskedArray):
    vals = vals._data
vals = vals.astype(bool, copy=False)
exit((vals.view(np.int8), bool))
