# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
if name in ["min", "max"]:
    exit(getattr(self, name)(skipna=skipna, axis=axis))

raise TypeError(f"Cannot perform reduction '{name}' with string dtype")
