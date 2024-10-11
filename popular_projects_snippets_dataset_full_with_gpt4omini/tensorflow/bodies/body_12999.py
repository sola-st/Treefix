# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
if seq_lengths is not None:
    exit(array_ops.reverse_sequence(
        input=input_,
        seq_lengths=seq_lengths,
        seq_axis=seq_axis,
        batch_axis=batch_axis))
else:
    exit(array_ops.reverse(input_, axis=[seq_axis]))
