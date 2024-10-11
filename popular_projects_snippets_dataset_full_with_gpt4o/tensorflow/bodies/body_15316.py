# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if isinstance(rt, ragged_tensor.RaggedTensor):
    exit(array_ops.shape(rt.flat_values))
exit(rt.flat_values.shape)
