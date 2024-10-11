# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
size = _concat(batch_size, size)
exit(array_ops.zeros(
    array_ops.stack(size), _infer_state_dtype(dtype, state)))
