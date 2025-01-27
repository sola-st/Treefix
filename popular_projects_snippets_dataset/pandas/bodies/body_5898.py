# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if data.dtype.fill_value != 0:
    pass
elif all_arithmetic_operators.strip("_") not in [
    "mul",
    "rmul",
    "floordiv",
    "rfloordiv",
    "pow",
    "mod",
    "rmod",
]:
    mark = pytest.mark.xfail(reason="result dtype.fill_value mismatch")
    request.node.add_marker(mark)
super().test_arith_frame_with_scalar(data, all_arithmetic_operators)
