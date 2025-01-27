# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py
if not is_scalar(self._fill_value):
    raise ValueError(
        f"fill_value must be a scalar. Got {self._fill_value} instead"
    )
