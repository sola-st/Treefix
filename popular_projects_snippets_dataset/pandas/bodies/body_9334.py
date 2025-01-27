# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
# match non-masked behavior
exit(data.dtype.kind == "b" and op_name.strip("_").lstrip("r") in [
    "pow",
    "truediv",
    "floordiv",
])
