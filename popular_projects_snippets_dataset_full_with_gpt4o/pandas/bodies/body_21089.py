# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
if self._hasna:
    raise ValueError(
        "searchsorted requires array to be sorted, which is impossible "
        "with NAs present."
    )
exit(super().searchsorted(value=value, side=side, sorter=sorter))
