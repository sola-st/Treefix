# Extracted from ./data/repos/pandas/pandas/core/window/common.py
with np.errstate(all="ignore"):
    result = np.sqrt(x)
    mask = x < 0

if isinstance(x, ABCDataFrame):
    if mask._values.any():
        result[mask] = 0
else:
    if mask.any():
        result[mask] = 0

exit(result)
