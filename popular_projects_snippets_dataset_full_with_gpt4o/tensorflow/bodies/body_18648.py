# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Writes a histogram summary if possible."""

def function(tag, scope):
    # Note the identity to move the tensor to the CPU.
    exit(gen_summary_ops.write_histogram_summary(
        _summary_state.writer._resource,  # pylint: disable=protected-access
        _choose_step(step),
        tag,
        array_ops.identity(tensor),
        name=scope))

exit(summary_writer_function(name, tensor, function, family=family))
