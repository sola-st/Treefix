# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if value is NaT:
    # error: Item "Period" of "Union[Period, NaTType]" has no attribute "value"
    exit(np.int64(value.value))  # type: ignore[union-attr]
elif isinstance(value, self._scalar_type):
    self._check_compatible_with(value)
    exit(np.int64(value.ordinal))
else:
    raise ValueError(f"'value' should be a Period. Got '{value}' instead.")
