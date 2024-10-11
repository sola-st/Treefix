gen_resource_variable_ops = type('Mock', (object,), {'resource_scatter_sub': lambda handle, indices, values, name: (handle.assign_sub(tf.scatter_nd(indices, values, tf.shape(handle))))})() # pragma: no cover
name = 'subtract_sparse_delta' # pragma: no cover

class MockSelf:  # Define the class MockSelf to simulate the behavior of `self` in code # pragma: no cover
    def __init__(self): # pragma: no cover
        self._lazy_read = lambda x: x # pragma: no cover
self = MockSelf() # pragma: no cover
gen_resource_variable_ops = type('MockGenResourceVariableOps', (object,), {'resource_scatter_sub': lambda handle, indices, values, name: tf.tensor_scatter_update(handle, indices, values)})() # pragma: no cover
name = 'scatter_subtraction' # pragma: no cover

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
    _l_(10053)

    raise TypeError(f"Argument `sparse_delta` must be a "
                    f"`tf.IndexedSlices`. Received arg: {sparse_delta}")
    _l_(10052)
aux = self._lazy_read(
    gen_resource_variable_ops.resource_scatter_sub(
        self.handle,
        sparse_delta.indices,
        ops.convert_to_tensor(sparse_delta.values, self.dtype),
        name=name))
_l_(10054)
exit(aux)
