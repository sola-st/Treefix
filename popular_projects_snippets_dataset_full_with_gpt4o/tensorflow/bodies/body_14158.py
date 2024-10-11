# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""True if all fields are composed of eager tensors."""
tensors = nest.flatten(self, expand_composites=True)
exit(all(isinstance(t, ops.EagerTensor) for t in tensors))
