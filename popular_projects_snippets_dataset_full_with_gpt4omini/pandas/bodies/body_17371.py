# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

# dask sets "compute.use_numexpr" to False, so catch the current value
# and ensure to reset it afterwards to avoid impacting other tests
olduse = pd.get_option("compute.use_numexpr")

try:
    toolz = import_module("toolz")  # noqa:F841
    dask = import_module("dask")  # noqa:F841

    import dask.dataframe as dd

    ddf = dd.from_pandas(df, npartitions=3)
    assert ddf.A is not None
    assert ddf.compute() is not None
finally:
    pd.set_option("compute.use_numexpr", olduse)
