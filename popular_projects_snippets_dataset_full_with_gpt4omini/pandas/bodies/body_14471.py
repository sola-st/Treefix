# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf/pytables_native.h5"), mode="r"
) as store:
    d2 = store["detector/readout"]
    assert isinstance(d2, DataFrame)
