# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
assert isinstance(old_output, (ops.Tensor, ops.Operation)), old_output
assert isinstance(new_output, (WrappedTensor, ops.Operation)), new_output
self._conversion_map[old_output] = new_output
