# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# Using a copy (the chain), fails
df = DataFrame(
    {
        "A": Series(range(2), dtype="int64"),
        "B": np.array(np.arange(2, 4), dtype=np.float64),
    }
)

if using_copy_on_write:
    # TODO(CoW) can we still warn here?
    df.loc[0]["A"] = -5
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        df.loc[0]["A"] = -5
