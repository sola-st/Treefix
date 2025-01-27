# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if not context.executing_eagerly():
    raise NotImplementedError(
        "__deepcopy__() is only available when eager execution is enabled.")
copied_variable = ResourceVariable(
    initial_value=self.read_value(),
    trainable=self._trainable,
    constraint=self._constraint,
    dtype=self._dtype,
    name=self._shared_name,
    distribute_strategy=self._distribute_strategy,
    synchronization=self.synchronization,
    aggregation=self.aggregation)
memo[self._unique_id] = copied_variable
exit(copied_variable)
