# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
if "dtype" in kwds:
    kwds["dtype"] = ensure_dtype_objs(kwds["dtype"])
exit(TextReader(StringIO(data), delimiter=",", header=None, **kwds))
