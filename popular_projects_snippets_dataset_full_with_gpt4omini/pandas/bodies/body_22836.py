# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
if arr_dtype is not None:
    arr = arr.view(arr_dtype)
if out_dtype is not None:
    out = out.view(out_dtype)
if fill_wrap is not None:
    # FIXME: if we get here with dt64/td64 we need to be sure we have
    #  matching resos
    if fill_value.dtype.kind == "m":
        fill_value = fill_value.astype("m8[ns]")
    else:
        fill_value = fill_value.astype("M8[ns]")
    fill_value = fill_wrap(fill_value)

f(arr, indexer, out, fill_value=fill_value)
