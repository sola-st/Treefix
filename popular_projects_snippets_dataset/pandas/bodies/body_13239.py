# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# We don't really care about the exact failure, the important thing is
# that the resource should be cleaned up afterwards (BUG #35566)
fname = datapath("io", "sas", "data", "corrupt.sas7bdat")
msg = "'SAS7BDATReader' object has no attribute 'row_count'"
with pytest.raises(AttributeError, match=msg):
    pd.read_sas(fname)
