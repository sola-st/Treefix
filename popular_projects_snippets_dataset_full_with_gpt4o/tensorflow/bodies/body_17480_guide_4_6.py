class MockVariable: # pragma: no cover
    handle = 'mock_handle' # pragma: no cover
    def _lazy_read(self, value): # pragma: no cover
        return value # pragma: no cover
 # pragma: no cover
self = MockVariable() # pragma: no cover
name = 'operation_name' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
from l3.Runtime import _l_
"""Subtracts `tf.IndexedSlices` from this variable.

    Args:
      sparse_delta: `tf.IndexedSlices` to be subtracted from this variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
if not isinstance(sparse_delta, indexed_slices.IndexedSlices):
    _l_(22263)

    raise TypeError(f"Argument `sparse_delta` must be a "
                    f"`tf.IndexedSlices`. Received arg: {sparse_delta}")
    _l_(22262)
aux = self._lazy_read(
    gen_resource_variable_ops.resource_scatter_sub(
        self.handle,
        sparse_delta.indices,
        ops.convert_to_tensor(sparse_delta.values, self.dtype),
        name=name))
_l_(22264)
exit(aux)
