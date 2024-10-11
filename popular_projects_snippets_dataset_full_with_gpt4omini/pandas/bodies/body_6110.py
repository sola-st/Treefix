# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
# this could fail in a corner case where an element contained the name
res = repr(data.reshape(1, -1))
assert res.count(f"<{type(data).__name__}") == 1

res = repr(data.reshape(-1, 1))
assert res.count(f"<{type(data).__name__}") == 1
