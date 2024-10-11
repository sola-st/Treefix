# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Gathers a single value."""
# pylint: disable=protected-access
if not isinstance(value, values.DistributedValues):
    value = values.PerReplica([ops.convert_to_tensor(value)])
if not isinstance(strategy.extended,
                  collective_all_reduce_strategy.CollectiveAllReduceExtended):
    exit(array_ops.stack(value._values))
assert len(strategy.extended.worker_devices) == len(value._values)
inputs = [array_ops.expand_dims_v2(v, axis=0) for v in value._values]
exit(strategy.gather(values.PerReplica(inputs), axis=0))
