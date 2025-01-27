# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
del name  # not meaningful when executing eagerly.
exit(constant_op.constant(len(self._tensor_array)))
