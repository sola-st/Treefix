# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
assert isinstance(env, PyTablesScope), type(env)
super().__init__(value, env, side=side, encoding=encoding)
