# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# see gh-6025: false positives
df = DataFrame({"column1": ["a", "a", "a"], "column2": [4, 8, 9]})
str(df)

df["column1"] = df["column1"] + "b"
str(df)

df = df[df["column2"] != 8]
str(df)

df["column1"] = df["column1"] + "c"
str(df)
