# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
# Note: this is expensive right now! The hope is that we can
# make this faster by having an optional mask, but not have to change
# source code using it..

# error: Incompatible return value type (got "bool_", expected "bool")
exit(self._mask.any())  # type: ignore[return-value]
