# Extracted from ./data/repos/pandas/pandas/core/ops/methods.py
for name, method in new_methods.items():
    setattr(cls, name, method)
