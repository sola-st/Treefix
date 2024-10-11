# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
bad_stream = b"foo"
if engine is None:
    error = ValueError
    msg = (
        "Excel file format cannot be determined, you must "
        "specify an engine manually."
    )
elif engine == "xlrd":
    from xlrd import XLRDError

    error = XLRDError
    msg = (
        "Unsupported format, or corrupt file: Expected BOF "
        "record; found b'foo'"
    )
else:
    error = BadZipFile
    msg = "File is not a zip file"
with pytest.raises(error, match=msg):
    pd.read_excel(bad_stream)
