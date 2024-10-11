# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# Check if the SAS file has zero variables (PR #18184)
fname = datapath("io", "sas", "data", "zero_variables.sas7bdat")
with pytest.raises(EmptyDataError, match="No columns to parse from file"):
    pd.read_sas(fname)
