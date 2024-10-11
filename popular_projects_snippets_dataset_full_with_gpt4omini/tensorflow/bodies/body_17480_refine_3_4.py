gen_resource_variable_ops = type('MockGenResourceVariableOps', (object,), {'resource_scatter_sub': lambda h, i, v, name: tf.raw_ops.ResourceScatterSub(variable=h, indices=i, updates=v, name=name)})() # pragma: no cover
name = 'scatter_subtract_op' # pragma: no cover

gen_resource_variable_ops = type('MockGenResourceVariableOps', (object,), {'resource_scatter_sub': lambda h, i, v, name: tf.tensor_scatter_nd_sub(h, tf.expand_dims(i, axis=-1), v)})() # pragma: no cover
ops = type('MockOps', (object,), {'convert_to_tensor': lambda value, dtype: tf.convert_to_tensor(value, dtype=dtype)})() # pragma: no cover
name = 'subtract_sparse_delta_operation' # pragma: no cover

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
