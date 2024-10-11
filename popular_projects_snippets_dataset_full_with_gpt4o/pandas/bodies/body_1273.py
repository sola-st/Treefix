# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# Doc example
df = DataFrame(
    {
        "a": ["one", "one", "two", "three", "two", "one", "six"],
        "c": Series(range(7), dtype="int64"),
    }
)
assert df._is_copy is None

if using_copy_on_write:
    # TODO(CoW) can we still warn here?
    indexer = df.a.str.startswith("o")
    df[indexer]["c"] = 42
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        indexer = df.a.str.startswith("o")
        df[indexer]["c"] = 42
