# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary._as_graph_element())  # pylint: disable=protected-access
# pylint: disable=protected-access
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    if ds_context.in_cross_replica_context():
        exit(ops.convert_to_tensor(self._get_cross_replica()))
exit(self._get()._as_graph_element())
