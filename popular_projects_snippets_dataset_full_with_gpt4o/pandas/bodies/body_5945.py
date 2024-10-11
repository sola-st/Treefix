# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
if len(data[0]) != 1:
    mark = pytest.mark.xfail(reason="raises in coercing to Series")
    request.node.add_marker(mark)
super().test_arith_frame_with_scalar(data, all_arithmetic_operators)
