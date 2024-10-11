# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
if name not in MATHOPS:
    raise ValueError(f'"{name}" is not a supported function')
self.name = name
self.func = getattr(np, name)
