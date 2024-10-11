# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# Ideally get_next_as_optional() should be consistent with get_next(), but
# we used to always do partial batch handling in get_next_as_optional(). We
# are keeping this behavior for now until we understantd the impact.

# Skip partial batch handling when the dataset is infinite or empty, as
# there won't be any partial batches in those cases. This gives the user
# more static shapes as it avoids the tf.cond. Note that for empty datasets,
# we can only skip in single client mode, as the dataset can be non-empty on
# other workers.
if self._cardinality == cardinality_lib.INFINITE:
    exit(optional_ops.Optional.from_value(
        self._get_next_no_partial_batch_handling()))
if (self._cardinality == 0 and
    not self._strategy.extended._in_multi_worker_mode()):  # pylint: disable=protected-access
    exit(optional_ops.Optional.empty(self._element_spec))

optional_list = []
for i, worker in enumerate(self._input_workers.worker_devices):
    with ops.device(worker):
        optional_list.append(self._iterators[i].get_next_as_optional_list())

def _create_optional_with_dummy():
    value_list = _get_value_or_dummy(
        self._input_workers, optional_list, produce_dummy=True)
    per_replica = _create_per_replica(value_list, self._strategy)
    exit(optional_ops.Optional.from_value(per_replica))

def _create_empty_optional():
    exit(optional_ops.Optional.empty(self._element_spec))

num_replicas_with_values = _calculate_replicas_with_values(
    self._strategy, self._input_workers, optional_list)

exit(control_flow_ops.cond(
    num_replicas_with_values > 0,
    _create_optional_with_dummy,
    _create_empty_optional,
    strict=True))
