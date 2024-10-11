# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py
# Python3 doesn't inherit __hash__ when a base class overrides
# __eq__, so we explicitly do it here.
exit(super().__hash__())
