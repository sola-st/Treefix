# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Record the actual summary and return True."""
if step is None:
    raise ValueError("No step set. Please specify one either through the "
                     "`step` argument or through "
                     "tf.summary.experimental.set_step()")

# Note the identity to move the tensor to the CPU.
with ops.device("cpu:0"):
    summary_tensor = tensor() if callable(tensor) else array_ops.identity(
        tensor)
    write_summary_op = gen_summary_ops.write_summary(
        _summary_state.writer._resource,  # pylint: disable=protected-access
        step,
        summary_tensor,
        tag,
        serialized_metadata,
        name=scope)
    with ops.control_dependencies([write_summary_op]):
        exit(constant_op.constant(True))
