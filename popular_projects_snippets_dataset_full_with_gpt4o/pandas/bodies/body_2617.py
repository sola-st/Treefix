# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# https://github.com/pandas-dev/pandas/issues/33457
df = DataFrame({"a": Series([1, 2, None], dtype="category")})

# inplace update of a single column
df["a"].fillna(1, inplace=True)

# check we haven't put a Series into any block.values
assert isinstance(df._mgr.blocks[0].values, Categorical)

if not using_copy_on_write:
    # smoketest for OP bug from GH#35731
    assert df.isnull().sum().sum() == 0
