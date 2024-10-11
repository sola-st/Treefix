# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
if isinstance(shape, ops.Tensor):
    exit(tensor_shape.as_shape(tensor_util.constant_value(shape)))
else:
    exit(shape)
