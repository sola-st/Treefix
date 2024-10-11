# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
exit(obj.base if getattr(obj, "base", None) is not None else obj)
