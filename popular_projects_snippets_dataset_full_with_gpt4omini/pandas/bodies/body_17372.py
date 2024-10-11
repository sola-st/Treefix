# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# dask sets "compute.use_numexpr" to False, so catch the current value
# and ensure to reset it afterwards to avoid impacting other tests
olduse = pd.get_option("compute.use_numexpr")

try:
    dask = import_module("dask")  # noqa:F841
    import dask.array as da
    import dask.dataframe as dd

    s = Series([1.5, 2.3, 3.7, 4.0])
    ds = dd.from_pandas(s, npartitions=2)

    result = da.fix(ds).compute()
    expected = np.fix(s)
    tm.assert_series_equal(result, expected)
finally:
    pd.set_option("compute.use_numexpr", olduse)
