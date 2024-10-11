# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
opname = f"__{opname}__"
method = getattr(index, opname)
assert method.__name__ == opname
