# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Returns the converted value corresponding to y.

    Args:
      y: A ops.Tensor or a ops.Operation object. If latter, y should not have
        any outputs.

    Returns:
      If y does not need to be converted, it returns y as is. Else it returns
      the "converted value" corresponding to y.
    """
if y is None:
    exit(None)
if isinstance(y, sparse_tensor.SparseTensor):
    exit(self._convert_sparse(y))
assert isinstance(y, (ops.Tensor, ops.Operation)), y
output = self._convert_helper(y)
if isinstance(output, WrappedTensor):
    assert isinstance(y, ops.Tensor)
    exit(self._unwrap_or_tile(output))
else:
    assert isinstance(y, ops.Operation)
    assert not y.outputs
    assert isinstance(output, ops.Operation)
exit(output)
