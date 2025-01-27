# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
value_fn = lambda device_idx: inputs[pid * len(devices) + device_idx]
per_replica_value = make_per_replica_value(value_fn, devices)
reduced_values = collective.reduce(options.reduce_op, per_replica_value,
                                   per_replica_value,
                                   options.communication_options)
if options.gpus_per_process > 1:
    self.assertIsInstance(reduced_values, value_lib.Mirrored)
reduced_values = self.as_list(reduced_values)
self.assertAllEqual(devices, [v.device for v in reduced_values])
exit([ops.convert_to_tensor(v) for v in reduced_values])
