# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if isinstance(self, ops.EagerTensor):
    exit(self._numpy().tolist())  # pylint: disable=protected-access

raise ValueError('Symbolic Tensors do not support the tolist API.')
