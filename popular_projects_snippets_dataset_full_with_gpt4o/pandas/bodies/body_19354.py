# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
if isinstance(other, str) and other == self.name:
    exit(True)
exit(super().__eq__(other))
