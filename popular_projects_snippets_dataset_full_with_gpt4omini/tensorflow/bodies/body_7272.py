# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = (
    options.prefer_unique_instance_key)
collective, devices, pid = self.make_collective(options.num_processes,
                                                options.gpus_per_process)

def batch_reduce_fn():
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

per_replica_expect = nest.map_structure(
    lambda x: [ops.convert_to_tensor(x)] * len(devices), expect)

if "eager" in options.mode:
    got = batch_reduce_fn()
    self.assertAllClose(got, per_replica_expect)

if "func_graph" in options.mode:
    got = def_function.function(batch_reduce_fn)()
    self.assertAllClose(got, per_replica_expect)
