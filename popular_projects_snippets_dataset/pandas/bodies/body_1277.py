# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# Implicitly take
df = random_text(100000)
indexer = df.letters.apply(lambda x: len(x) > 10)
df = df.loc[indexer]

assert df._is_copy is not None
df["letters"] = df["letters"].apply(str.lower)
