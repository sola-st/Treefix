# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Generates a random tensor based on the data type and tensor shape."""
shape = _get_concrete_tensor_shape(tensor.shape.as_proto(), batch_size)
exit(_generate_random_tensor_ops(
    shape=shape, dtype=tensor.dtype, name=tensor.name))
