# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH #19474
# assigning like "df.iloc[0, [0]] = ['Z']" should be evaluated
# elementwisely, not using "setter('A', ['Z'])".

df = DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
df.iloc[0, indexer] = value
result = df.iloc[0, 0]

assert is_scalar(result) and result == "Z"
