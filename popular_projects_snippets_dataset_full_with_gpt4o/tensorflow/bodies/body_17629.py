# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
shape = tensor_shape.unknown_shape()
for i in inputs:
    if isinstance(i, ops.Tensor):
        shape = shape.merge_with(i.get_shape())
exit(shape)
