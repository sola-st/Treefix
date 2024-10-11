# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = (
    options.prefer_unique_instance_key)
collective, devices, pid = self.make_collective(options.num_processes,
                                                options.gpus_per_process)

def reduce_fn():
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

per_replica_expect = [ops.convert_to_tensor(expect)] * len(devices)

if "eager" in options.mode:
    got = reduce_fn()
    self.assertAllClose(got, per_replica_expect)

if "func_graph" in options.mode:
    got = def_function.function(reduce_fn)()
    self.assertAllClose(got, per_replica_expect)
