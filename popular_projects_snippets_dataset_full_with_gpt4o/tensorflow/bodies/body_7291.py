# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
per_replica_value = make_per_replica_value(value, devices)
gathered_values = collective._gather(
    per_replica_value, per_replica_value, axis=axis, options=options)
gathered_values = self.as_list(gathered_values)
# Skip checking devices in eager. In eager the device attribute doesn't
# reflect the actual device of the tensor.
if not context.executing_eagerly():
    self.assertAllEqual(devices, [v.device for v in gathered_values])
exit([ops.convert_to_tensor(v) for v in gathered_values])
