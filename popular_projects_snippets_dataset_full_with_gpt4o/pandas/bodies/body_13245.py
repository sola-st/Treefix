# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
"""Errors in RLE/RDC decompression should propagate."""
with open(datapath("io", "sas", "data", test_file), "rb") as fd:
    data = bytearray(fd.read())
data[override_offset] = override_value
with pytest.raises(Exception, match=expected_msg):
    pd.read_sas(io.BytesIO(data), format="sas7bdat")
