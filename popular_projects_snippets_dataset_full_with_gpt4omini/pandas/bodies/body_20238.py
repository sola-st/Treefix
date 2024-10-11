# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
self.include = include
self.exclude = exclude

if obj.ndim == 2 and obj.columns.size == 0:
    raise ValueError("Cannot describe a DataFrame without columns")

super().__init__(obj)
