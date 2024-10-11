# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
msg = "Support for generic buffers has not been implemented."
with pytest.raises(NotImplementedError, match=msg):
    read_hdf(BytesIO(b""), "df")
