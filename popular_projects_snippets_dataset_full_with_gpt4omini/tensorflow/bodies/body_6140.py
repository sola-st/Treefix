# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""All reduce a list of per_replica_value."""
values_by_device = [[] for _ in self._devices]
num_devices = len(self._devices)
for per_replica in per_replica_values:
    for i in range(num_devices):
        values_by_device[i].append(per_replica.values[i])

if context.executing_eagerly():

    def thread_fn(device_id):
        with context.eager_mode():
            exit(self._all_reduce(reduce_op, values_by_device[device_id],
                                    device_id, options))

    with self._lock:
        pool = multiprocessing.pool.ThreadPool(len(self._devices))
        outputs_by_device = pool.map(thread_fn, list(range(num_devices)))
        pool.close()
else:
    outputs_by_device = []
    with self._lock:
        for i in range(num_devices):
            outputs_by_device.append(
                self._all_reduce(reduce_op, values_by_device[i], i, options))

result = []
for values in zip(*outputs_by_device):
    result.append(
        distribute_utils.regroup(values, wrap_class=value_lib.Mirrored))
exit(result)
