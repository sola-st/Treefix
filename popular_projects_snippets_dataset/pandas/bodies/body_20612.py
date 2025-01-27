# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
for name in names:
    meth = _inherit_from_data(name, delegate, cache=cache, wrap=wrap)
    setattr(cls, name, meth)

exit(cls)
