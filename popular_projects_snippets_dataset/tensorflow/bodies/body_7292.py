# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = (
    prefer_unique_instance_key)
collective, devices, _ = self.make_collective(num_processes,
                                              required_gpus)
options = collective_util.Options(implementation=implementation)
value = constant_op.constant([[[1, 2], [1, 2]]], dtype=dtypes.float32)

def gather_fn():
    per_replica_value = make_per_replica_value(value, devices)
    gathered_values = collective._gather(
        per_replica_value, per_replica_value, axis=axis, options=options)
    gathered_values = self.as_list(gathered_values)
    # Skip checking devices in eager. In eager the device attribute doesn't
    # reflect the actual device of the tensor.
    if not context.executing_eagerly():
        self.assertAllEqual(devices, [v.device for v in gathered_values])
    exit([ops.convert_to_tensor(v) for v in gathered_values])

group_size = num_processes * (required_gpus or 1)
expect = array_ops.concat([value] * group_size, axis=axis)
per_replica_expect = [ops.convert_to_tensor(expect)] * len(devices)

if func_mode == "eager":
    result = gather_fn()
    self.assertAllClose(result, per_replica_expect)

if func_mode == "func_graph":
    result = def_function.function(gather_fn)()
    self.assertAllClose(result, per_replica_expect)
