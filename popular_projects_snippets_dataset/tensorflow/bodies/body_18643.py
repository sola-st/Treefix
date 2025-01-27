# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
if metadata is None:
    serialized_metadata = constant_op.constant("")
elif hasattr(metadata, "SerializeToString"):
    serialized_metadata = constant_op.constant(metadata.SerializeToString())
else:
    serialized_metadata = metadata
# Note the identity to move the tensor to the CPU.
exit(gen_summary_ops.write_summary(
    _summary_state.writer._resource,  # pylint: disable=protected-access
    _choose_step(step),
    array_ops.identity(tensor),
    tag,
    serialized_metadata,
    name=scope))
