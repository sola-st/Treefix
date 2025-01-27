# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
seq_lengths = op.inputs[1]
exit([
    array_ops.reverse_sequence(
        grad,
        batch_axis=op.get_attr("batch_dim"),
        seq_axis=op.get_attr("seq_dim"),
        seq_lengths=seq_lengths), None
])
