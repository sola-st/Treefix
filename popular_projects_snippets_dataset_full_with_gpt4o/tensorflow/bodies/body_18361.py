# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Creates an object to rewrite a parallel-for loop.

    Args:
      loop_var: ops.Tensor output of a Placeholder operation. The value should
        be an int32 scalar representing the loop iteration number.
      loop_len: A scalar or scalar Tensor representing the number of iterations
        the loop is run for.
      pfor_ops: List of all ops inside the loop body.
      fallback_to_while_loop: If True, on failure to vectorize an op, a while
        loop is used to sequentially execute that op.
      all_indices: If not None, an int32 vector with size `loop_len`
        representing the iteration ids that are still active. These values
        should be unique and sorted. However they may not be contiguous. This is
        typically the case when inside a control flow construct which has
        partitioned the indices of the iterations that are being converted.
      all_indices_partitioned: If True, this object is being constructed from a
        control flow construct where not all the pfor iterations are guaranteed
        to be active.
      pfor_config: PForConfig object used while constructing the loop body.
      warn: Whether or not to warn on while loop conversions.
    """
assert isinstance(loop_var, ops.Tensor)
assert loop_var.op.type == "PlaceholderWithDefault"
self._loop_var = loop_var
loop_len_value = tensor_util.constant_value(loop_len)
if loop_len_value is not None:
    loop_len = loop_len_value
self._loop_len_vector = array_ops.reshape(loop_len, [1])
self._all_indices_partitioned = all_indices_partitioned
if all_indices_partitioned:
    assert all_indices is not None
self.all_indices = (
    math_ops.range(loop_len) if all_indices is None else all_indices)

self._conversion_map = object_identity.ObjectIdentityDictionary()
self._conversion_map[loop_var] = wrap(self.all_indices, True)
self._pfor_ops = set(pfor_ops)
self._pfor_op_ids = set(x._id for x in pfor_ops)
self._fallback_to_while_loop = fallback_to_while_loop
self._warn = warn
self._pfor_config = pfor_config
