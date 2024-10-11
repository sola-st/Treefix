class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
    def _lazy_read(self, x): # pragma: no cover
        return x # pragma: no cover
self = MockSelf() # pragma: no cover
class MockGenResourceVariableOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def resource_scatter_sub(handle, indices, updates, name=None): # pragma: no cover
        return tf.tensor_scatter_nd_sub(tf.Variable(handle), tf.expand_dims(indices, axis=-1), updates) # pragma: no cover
gen_resource_variable_ops = MockGenResourceVariableOps() # pragma: no cover
class MockOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def convert_to_tensor(value, dtype=None): # pragma: no cover
        return tf.convert_to_tensor(value, dtype=dtype) # pragma: no cover
ops = MockOps() # pragma: no cover
name = 'subtraction_operation' # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
    def _lazy_read(self, x): # pragma: no cover
        return x # pragma: no cover
self = MockSelf() # pragma: no cover
class MockGenResourceVariableOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def resource_scatter_sub(handle, indices, updates, name=None): # pragma: no cover
        return tf.tensor_scatter_nd_sub(handle, tf.expand_dims(indices, axis=-1), updates) # pragma: no cover
gen_resource_variable_ops = MockGenResourceVariableOps() # pragma: no cover
class MockOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def convert_to_tensor(value, dtype=None): # pragma: no cover
        return tf.convert_to_tensor(value, dtype=dtype) # pragma: no cover
ops = MockOps() # pragma: no cover
name = 'subtract_sparse_delta' # pragma: no cover

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
