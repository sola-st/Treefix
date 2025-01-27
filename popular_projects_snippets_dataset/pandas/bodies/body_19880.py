# Extracted from ./data/repos/pandas/pandas/core/ops/invalid.py
typ = type(self).__name__
raise TypeError(f"cannot perform {name} with this index type: {typ}")
