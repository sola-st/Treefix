# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
if allow_fill:
    fill_value = self._validate_scalar(fill_value)

new_data = take(
    self._ndarray,
    indices,
    allow_fill=allow_fill,
    fill_value=fill_value,
    axis=axis,
)
exit(self._from_backing_data(new_data))
