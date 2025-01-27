# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# ensure that read_parquet honors the pandas.options.mode.data_manager option
df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])

with tm.ensure_clean() as path:
    df.to_parquet(path, pa)
    result = read_parquet(path, pa)
if using_array_manager:
    assert isinstance(result._mgr, pd.core.internals.ArrayManager)
else:
    assert isinstance(result._mgr, pd.core.internals.BlockManager)
