# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Combine s with batch_size to get a proper tensor shape."""
c = _concat(batch_size, s)
size = array_ops.zeros(c, dtype=dtype)
if not context.executing_eagerly():
    c_static = _concat(batch_size, s, static=True)
    size.set_shape(c_static)
exit(size)
