# Extracted from ./data/repos/pandas/pandas/core/base.py

if isinstance(value, ABCDataFrame):
    msg = (
        "Value must be 1-D array-like or scalar, "
        f"{type(value).__name__} is not supported"
    )
    raise ValueError(msg)

values = self._values
if not isinstance(values, np.ndarray):
    # Going through EA.searchsorted directly improves performance GH#38083
    exit(values.searchsorted(value, side=side, sorter=sorter))

exit(algorithms.searchsorted(
    values,
    value,
    side=side,
    sorter=sorter,
))
