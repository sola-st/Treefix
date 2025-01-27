# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_multi_gpu_test.py
local_devices = device_lib.list_local_devices()
gpu_device_names = []
for device in local_devices:
    if device.device_type == "GPU":
        gpu_device_names.append(device.name)
gpu_device_names = sorted(gpu_device_names)

if len(gpu_device_names) < 2:
    self.skipTest(
        "This test requires at least 2 GPUs, but only %d is available." %
        len(gpu_device_names))

with session.Session() as sess:
    v = variables.Variable([10.0, 15.0], dtype=dtypes.float32, name="v")
    with ops.device(gpu_device_names[0]):
        u0 = math_ops.add(v, v, name="u0")
    with ops.device(gpu_device_names[1]):
        u1 = math_ops.multiply(v, v, name="u1")
    w = math_ops.subtract(u1, u0, name="w")

    self.evaluate(v.initializer)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(run_options, sess.graph,
                            debug_urls="file://" + self._dump_root)
    run_metadata = config_pb2.RunMetadata()
    self.assertAllClose(
        [80.0, 195.0],
        sess.run(w, options=run_options, run_metadata=run_metadata))

    debug_dump_dir = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)
    self.assertEqual(3, len(debug_dump_dir.devices()))
    self.assertAllClose(
        [10.0, 15.0], debug_dump_dir.get_tensors("v", 0, "DebugIdentity")[0])
    self.assertAllClose(
        [20.0, 30.0], debug_dump_dir.get_tensors("u0", 0, "DebugIdentity")[0])
    self.assertAllClose(
        [100.0, 225.0],
        debug_dump_dir.get_tensors("u1", 0, "DebugIdentity")[0])
