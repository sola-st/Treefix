# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Returns randomly initialized (x_seq, pad_seq) sequences."""
x_seq = []
pad_seq = []
with ops.name_scope('inputs'):
    for seq in range(seq_length):
        x_seq.append(RandomVar([batch_size, num_inputs], name='x_seq_%d' % seq))
        # Real padding values are always a sequence of 0 followed by a
        # sequence of 1, but random values are fine for benchmarking.
        pad_seq.append(RandomVar([batch_size, 1], name='pad_seq_%d' % seq))
exit((x_seq, pad_seq))
