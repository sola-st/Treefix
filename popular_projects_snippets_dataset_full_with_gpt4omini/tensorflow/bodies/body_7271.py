# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
batch_size = len(inputs[0])
value_dst_pairs = []
for i in range(batch_size):

    def value_fn(device_idx, idx=i):
        exit(inputs[pid * len(devices) + device_idx][idx])

    per_replica_value = make_per_replica_value(value_fn, devices)
    value_dst_pairs.append((per_replica_value, per_replica_value))
reduced_values = collective.batch_reduce(options.reduce_op,
                                         value_dst_pairs,
                                         options.communication_options)
if options.gpus_per_process > 1:
    for v in reduced_values:
        self.assertIsInstance(v, value_lib.Mirrored)
reduced_values = [self.as_list(v) for v in reduced_values]
for v in reduced_values:
    self.assertAllEqual(devices, [t.device for t in v])
exit(nest.map_structure(ops.convert_to_tensor, reduced_values))
