# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
"""Perform one optimization step."""
# Run forward & backward to get gradients, variables list.
g_v = d.extended.call_for_each_replica(grad_fn, args=(one,))

# Update the variables using the gradients and the update() function.
before_list = []
after_list = []
for g, v in g_v:
    fetched = d.extended.read_var(v)
    before_list.append(fetched)
    # control_dependencies irrelevant but harmless in eager execution
    with ops.control_dependencies([fetched]):
        g = d.extended.reduce_to(
            reduce_util.ReduceOp.SUM, g, destinations=v)
        with ops.control_dependencies(
            d.extended.update(v, update, args=(g,), group=False)):
            after_list.append(d.extended.read_var(v))
exit((before_list, after_list))
