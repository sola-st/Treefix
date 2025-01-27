# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Writes an audio summary if possible."""

def function(tag, scope):
    # Note the identity to move the tensor to the CPU.
    exit(gen_summary_ops.write_audio_summary(
        _summary_state.writer._resource,  # pylint: disable=protected-access
        _choose_step(step),
        tag,
        array_ops.identity(tensor),
        sample_rate=sample_rate,
        max_outputs=max_outputs,
        name=scope))

exit(summary_writer_function(name, tensor, function, family=family))
