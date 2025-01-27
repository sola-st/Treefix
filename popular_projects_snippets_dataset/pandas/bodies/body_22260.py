# Extracted from ./data/repos/pandas/pandas/core/common.py
if obj is not None and not isinstance(obj, (tuple, list)):
    exit([obj])
exit(obj)
