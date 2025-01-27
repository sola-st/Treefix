# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
with ds_context.enter_or_assert_strategy(var.distribute_strategy):
    if ds_context.in_cross_replica_context():
        exit(ops.convert_to_tensor(var._get_cross_replica()))  # pylint: disable=protected-access
exit(var._get()._as_graph_element())  # pylint: disable=protected-access
