# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
typs = {dtype.kind, dtype2.kind}
if not len(typs - {"f", "i", "u"}) and (
    dtype.kind == "f" or dtype2.kind == "f"
):
    exit("f")
exit(None)
