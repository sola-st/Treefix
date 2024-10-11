# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Record the actual summary and return True."""
# Note the identity to move the tensor to the CPU.
with ops.device("cpu:0"):
    raw_summary_op = gen_summary_ops.write_raw_proto_summary(
        _summary_state.writer._resource,  # pylint: disable=protected-access
        step,
        array_ops.identity(tensor),
        name=scope)
    with ops.control_dependencies([raw_summary_op]):
        exit(constant_op.constant(True))
