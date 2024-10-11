# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 3880
df = DataFrame([[1, 1], [1, 1]])
df.index.name = "index_name"
result = df.iloc[[0, 1]].index.name
assert result == "index_name"

result = df.loc[[0, 1]].index.name
assert result == "index_name"
