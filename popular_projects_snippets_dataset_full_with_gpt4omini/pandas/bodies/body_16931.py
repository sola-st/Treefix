# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# #980
df1 = DataFrame(columns=["A", "B", "C"])
df1 = df1.set_index(["A"])
df2 = DataFrame(data=[[1, 4, 7], [2, 5, 8], [3, 6, 9]], columns=["A", "B", "C"])
df2 = df2.set_index(["A"])

result = df1._append(df2)
assert result.index.name == "A"
