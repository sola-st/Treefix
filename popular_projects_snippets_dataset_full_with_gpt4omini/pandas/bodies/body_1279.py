# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

df = random_text(100000)
indexer = df.letters.apply(lambda x: len(x) > 10)
df.loc[indexer, "letters"] = df.loc[indexer, "letters"].apply(str.lower)
