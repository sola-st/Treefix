# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Trace function for detecting any NaN/Inf in the tensor."""

if tensor.dtype.is_floating:
    mask = math_ops.reduce_any(
        gen_math_ops.logical_or(
            gen_math_ops.is_nan(tensor), gen_math_ops.is_inf(tensor)))
    output_tensor = control_flow_ops.cond(
        mask,
        lambda: constant_op.constant([1.0]),
        lambda: constant_op.constant([0.0]))
else:
    output_tensor = constant_op.constant([0.0])
exit(output_tensor)
