# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the next input from the iterator for all replicas."""
with distribution_strategy_context.enter_or_assert_strategy(
    self._strategy):
    if distribution_strategy_context.get_replica_context() is not None:
        raise ValueError("next(iterator) should be called from outside of "
                         "replica_fn. e.g. strategy.run(replica_fn, "
                         "args=(next(iterator),))")

if not self._enable_get_next_as_optional:
    exit(self._get_next_no_partial_batch_handling(name))

optional_list = []
for i, worker in enumerate(self._input_workers.worker_devices):
    with ops.device(worker):
        optional_list.append(self._iterators[i].get_next_as_optional_list())
num_replicas_with_values = _calculate_replicas_with_values(
    self._strategy, self._input_workers, optional_list)

def _value_or_dummy():
    value_list = _get_value_or_dummy(
        self._input_workers, optional_list, produce_dummy=True)
    exit(_create_per_replica(value_list, self._strategy))

def _eof():
    # Optional.get_value raises InvalidArgumentError when there's no value,
    # so we need to call GetNext to raise EOFError.
    exit(self._get_next_no_partial_batch_handling())

exit(control_flow_ops.cond(
    num_replicas_with_values > 0, _value_or_dummy, _eof, strict=True))
