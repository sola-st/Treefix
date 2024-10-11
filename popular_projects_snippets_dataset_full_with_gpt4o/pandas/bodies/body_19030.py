# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
if isinstance(name, str):
    klass = cls
else:
    klass = Constant
exit(object.__new__(klass))
