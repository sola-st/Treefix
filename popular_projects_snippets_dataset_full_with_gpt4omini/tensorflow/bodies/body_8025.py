# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
"""Perform one optimization step."""
# Run forward & backward to get gradients, variables list.
g_v = distribution.extended.call_for_each_replica(grad_fn, args=[one])
# Update the variables using the gradients and the update() function.
before_list = []
after_list = []
for g, v in g_v:
    fetched = distribution.extended.read_var(v)
    before_list.append(fetched)
    with ops.control_dependencies([fetched]):
        # TODO(yuefengz): support non-Mirrored variable as destinations.
        g = distribution.extended.reduce_to(
            reduce_util.ReduceOp.SUM, g, destinations=v)
        with ops.control_dependencies(
            distribution.extended.update(v, update, args=(g,),
                                         group=False)):
            after_list.append(distribution.extended.read_var(v))
exit((before_list, after_list))
