# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# e.g. "ns", "us", "ms"
# error: Argument 1 to "dtype_to_unit" has incompatible type
# "ExtensionDtype"; expected "Union[DatetimeTZDtype, dtype[Any]]"
exit(dtype_to_unit(self.dtype))  # type: ignore[arg-type]
