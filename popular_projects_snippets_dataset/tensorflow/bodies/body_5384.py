# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if (self._aggregation != vs.VariableAggregation.ONLY_FIRST_REPLICA and
    self._aggregation != vs.VariableAggregation.NONE):
    raise NotImplementedError(
        values_util.scatter_error_msg.format(
            op_name="scatter_update", aggregation=self._aggregation))
exit(values_util.scatter_update(
    var, sparse_delta, use_locking=use_locking, name=name))
