# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reshape.py
result = idx[:3].append(idx[3:])
assert result.equals(idx)

foos = [idx[:1], idx[1:3], idx[3:]]
result = foos[0].append(foos[1:])
assert result.equals(idx)

# empty
result = idx.append([])
assert result.equals(idx)
