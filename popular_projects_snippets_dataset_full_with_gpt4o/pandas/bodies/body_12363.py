# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
dta_file = datapath("io", "data", "stata", "stata-dta-partially-labeled.dta")
with pytest.raises(ValueError, match="chunksize must be a positive"):
    with StataReader(dta_file, chunksize=chunksize):
        pass
