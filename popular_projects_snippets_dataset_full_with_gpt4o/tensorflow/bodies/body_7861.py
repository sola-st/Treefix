# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
self._distribute_strategy = strategy
self._v = v
# NOTE: We don't use "_distributed_container" here because we don't want
# to trigger that code path in regroup().
v._aggregating_container = weakref.ref(self)  # pylint: disable=protected-access
self._aggregation = aggregation
