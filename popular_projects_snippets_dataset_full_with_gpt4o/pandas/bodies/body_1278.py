# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
if using_copy_on_write:
    pytest.skip("_is_copy is not always set for CoW")
# Implicitly take 2
df = random_text(100000)
indexer = df.letters.apply(lambda x: len(x) > 10)

df = df.loc[indexer]
assert df._is_copy is not None
df.loc[:, "letters"] = df["letters"].apply(str.lower)

# with the enforcement of #45333 in 2.0, the .loc[:, letters] setting
#  is inplace, so df._is_copy remains non-None.
assert df._is_copy is not None

df["letters"] = df["letters"].apply(str.lower)
assert df._is_copy is None
