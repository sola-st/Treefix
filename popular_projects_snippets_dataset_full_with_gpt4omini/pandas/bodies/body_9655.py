# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
result = data + 1
assert not tm.shares_memory(result, data)
