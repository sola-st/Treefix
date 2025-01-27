# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py
"""Returns all-reduced gradients aggregated via summation.

  Args:
    grads_and_vars: List of (gradient, variable) pairs.

  Returns:
    List of (gradient, variable) pairs where gradients have been all-reduced.
  """
grads_and_vars = list(grads_and_vars)
filtered_grads_and_vars = filter_empty_gradients(grads_and_vars)
if filtered_grads_and_vars:
    if strategy_supports_no_merge_call():
        grads = [pair[0] for pair in filtered_grads_and_vars]
        reduced = distribute_ctx.get_strategy().extended._replica_ctx_all_reduce(  # pylint: disable=protected-access
            ds_reduce_util.ReduceOp.SUM, grads)
    else:
        # TODO(b/183257003): Remove this branch
        reduced = distribute_ctx.get_replica_context().merge_call(
            _all_reduce_sum_fn, args=(filtered_grads_and_vars,))
else:
    reduced = []
# Copy 'reduced' but add None gradients back in
reduced_with_nones = []
reduced_pos = 0
for g, v in grads_and_vars:
    if g is None:
        reduced_with_nones.append((None, v))
    else:
        reduced_with_nones.append((reduced[reduced_pos], v))
        reduced_pos += 1
assert reduced_pos == len(reduced), "Failed to add all gradients"
exit(reduced_with_nones)
