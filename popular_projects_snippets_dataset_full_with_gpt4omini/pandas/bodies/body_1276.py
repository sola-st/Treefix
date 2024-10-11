# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# gh-5597: a spurious raise as we are setting the entire column here

df = random_text(100000)

# Always a copy
x = df.iloc[[0, 1, 2]]
assert x._is_copy is not None

x = df.iloc[[0, 1, 2, 4]]
assert x._is_copy is not None

# Explicitly copy
indexer = df.letters.apply(lambda x: len(x) > 10)
df = df.loc[indexer].copy()

assert df._is_copy is None
df["letters"] = df["letters"].apply(str.lower)
