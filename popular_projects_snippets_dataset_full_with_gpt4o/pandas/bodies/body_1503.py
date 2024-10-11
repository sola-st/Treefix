# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH #19474
# assigning like "df.loc[0, ['A']] = ['Z']" should be evaluated
# elementwisely, not using "setter('A', ['Z'])".

df = DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
df.loc[0, indexer] = value
result = df.loc[0, "A"]

assert is_scalar(result) and result == "Z"
