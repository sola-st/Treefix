# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
# overwriting to indicate ops don't raise an error
exc = None
if op_name.strip("_").lstrip("r") in ["pow", "truediv", "floordiv"]:
    # match behavior with non-masked bool dtype
    exc = NotImplementedError
super().check_opname(s, op_name, other, exc=exc)
