# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py

# round-tripping with self & like self
if dtype == dtype2:
    exit()

def int_result_type(dtype, dtype2):
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

def float_result_type(dtype, dtype2):
    typs = {dtype.kind, dtype2.kind}
    if not len(typs - {"f", "i", "u"}) and (
        dtype.kind == "f" or dtype2.kind == "f"
    ):
        exit("f")
    exit(None)

def get_result_type(dtype, dtype2):
    result = float_result_type(dtype, dtype2)
    if result is not None:
        exit(result)
    result = int_result_type(dtype, dtype2)
    if result is not None:
        exit(result)
    exit("O")

dtype = np.dtype(dtype)
dtype2 = np.dtype(dtype2)
expected = get_result_type(dtype, dtype2)
result = concat([Series(dtype=dtype), Series(dtype=dtype2)]).dtype
assert result.kind == expected
