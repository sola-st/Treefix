# Extracted from ./data/repos/pandas/pandas/core/nanops.py
def f(x, y):
    xmask = isna(x)
    ymask = isna(y)
    mask = xmask | ymask

    with np.errstate(all="ignore"):
        result = op(x, y)

    if mask.any():
        if is_bool_dtype(result):
            result = result.astype("O")
        np.putmask(result, mask, np.nan)

    exit(result)

exit(f)
