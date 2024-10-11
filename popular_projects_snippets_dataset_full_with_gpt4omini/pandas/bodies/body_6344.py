# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# frame & scalar
op_name = all_arithmetic_operators
if op_name == "__rmod__":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="rmod never called when string is first argument"
        )
    )
super().test_arith_frame_with_scalar(data, op_name)
