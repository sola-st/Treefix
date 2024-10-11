ops = type('MockOps', (object,), {'convert_to_tensor': lambda x, dtype: tf.convert_to_tensor(x, dtype=dtype)})() # pragma: no cover
name = 'subtract_sparse_delta' # pragma: no cover

gen_resource_variable_ops = type('MockGenResourceVariableOps', (object,), {'resource_scatter_sub': lambda handle, indices, updates, name: tf.tensor_scatter_nd_update(handle, tf.expand_dims(indices, axis=-1), updates)})() # pragma: no cover
ops = type('MockOps', (object,), {'convert_to_tensor': lambda x, dtype: tf.convert_to_tensor(x, dtype=dtype)})() # pragma: no cover
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
