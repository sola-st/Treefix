# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
typs = {dtype.kind, dtype2.kind}
if not len(typs - {"i", "u", "b"}) and (
    dtype.kind == "i" or dtype2.kind == "i"
):
    exit("i")
elif not len(typs - {"u", "b"}) and (
    dtype.kind == "u" or dtype2.kind == "u"
):
    exit("u")
exit(None)
