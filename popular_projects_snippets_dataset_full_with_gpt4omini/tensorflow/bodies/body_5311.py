# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if values_util.is_saving_non_distributed():
    exit(self._primary.scatter_min(*args, **kwargs))
if (self._aggregation != vs.VariableAggregation.ONLY_FIRST_REPLICA and
    self._aggregation != vs.VariableAggregation.NONE):
    raise NotImplementedError(
        values_util.scatter_error_msg.format(
            op_name="scatter_min", aggregation=self._aggregation))
exit(super(MirroredVariable, self).scatter_min(*args, **kwargs))
