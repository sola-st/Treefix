# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
with context.eager_mode():
    exit(self._all_reduce(reduce_op, values_by_device[device_id],
                            device_id, options))
