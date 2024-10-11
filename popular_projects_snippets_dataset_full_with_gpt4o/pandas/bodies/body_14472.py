# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "pytables_native2.h5"), mode="r"
) as store:
    str(store)
    d1 = store["detector"]
    assert isinstance(d1, DataFrame)
