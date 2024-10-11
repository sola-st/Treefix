# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
if value.dtype.kind == "O":
    if allow_complex:
        value = value.astype("c16")
    else:
        value = value.astype("f8")
exit(func(value, **kwargs))
