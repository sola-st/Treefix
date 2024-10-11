# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Cast a single Tensor or TensorSpec to the compute dtype."""
if self._should_cast_single_input(x):
    exit(math_ops.cast(x, self._compute_dtype_object))
else:
    exit(x)
