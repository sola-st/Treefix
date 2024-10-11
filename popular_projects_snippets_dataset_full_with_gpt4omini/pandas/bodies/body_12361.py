# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
df = DataFrame({"cats": Series(["a", "b", "a", "b", "c"], dtype="category")})
df.index.name = "index"

expected = df.copy()
expected.index = expected.index.astype(np.int32)

with tm.ensure_clean() as path:
    df.to_stata(path, version=version)
    with StataReader(path, chunksize=2, order_categoricals=False) as reader:
        for i, block in enumerate(reader):
            block = block.set_index("index")
            assert "cats" in block
            tm.assert_series_equal(
                block.cats, expected.cats.iloc[2 * i : 2 * (i + 1)]
            )
