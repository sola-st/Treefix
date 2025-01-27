# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
opname = all_arithmetic_operators
if data.dtype.numpy_dtype == object and opname not in ["__add__", "__radd__"]:
    mark = pytest.mark.xfail(reason="Fails for object dtype")
    request.node.add_marker(mark)
super().test_arith_series_with_array(data, all_arithmetic_operators)
