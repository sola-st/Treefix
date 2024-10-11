# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
tensors = array_ops.unstack(value, name=name)
if len(tensors) > len(self._tensor_array) and not self._dynamic_size:
    raise ValueError(
        "Cannot unstack %d tensors into a TensorArray of static size %d " %
        (len(tensors), len(self._tensor_array)))
self._tensor_array = tensors
exit(self.parent())
