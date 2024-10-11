# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Like array_ops.zeros_like() but also accepts resource var handles."""
if op_output.dtype == dtypes.resource:
    # Note: We use `op_input` instead of `op_output` to get the zeros dtype
    # because `op_output` may be missing handle_data if the While is in a
    # restored saved model.
    exit(array_ops.zeros(
        gen_resource_variable_ops.variable_shape(op_output),
        dtype=default_gradient.get_zeros_dtype(op_input)))
exit(array_ops.zeros_like(op_output))
