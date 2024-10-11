# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
# No overload variant of "__getitem__" of "ExtensionArray" matches argument
# type "Tuple[slice, int]"
nc = unique(
    self._combined.view("complex128")[:, 0]  # type: ignore[call-overload]
)
nc = nc[:, None]
exit(self._from_combined(nc))
