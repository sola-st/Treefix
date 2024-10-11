# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""The loop body of map_fn.

      Args:
        i: the loop counter
        tas: the flat TensorArray accumulator list

      Returns:
        (i + 1, tas): the updated counter + updated TensorArrays

      Raises:
        TypeError: if fn_output_signature and result_value structure don't match
        ValueType: if fn_output_signature and result_value lengths don't match
      """
elems_value_batchable = [ta.read(i) for ta in elems_batchable_ta]
elems_value_flat = _elems_value_batchable_to_flat(elems_value_batchable,
                                                  elems_flat_signature)
elems_value = elems_unflatten(elems_value_flat)
ag_ctx = autograph_ctx.control_status_ctx()
autographed_fn = autograph.tf_convert(fn, ag_ctx)
result_value = autographed_fn(elems_value)
nest.assert_same_structure(fn_output_signature or elems, result_value)
result_value_flat = nest.flatten(result_value)
result_value_batchable = _result_value_flat_to_batchable(
    result_value_flat, result_flat_signature)
tas = [
    ta.write(i, value) for (ta, value) in zip(tas, result_value_batchable)
]
exit((i + 1, tas))
