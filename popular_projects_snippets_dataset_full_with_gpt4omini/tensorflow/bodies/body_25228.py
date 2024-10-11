# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
cls._dump_root = tempfile.mkdtemp()

cls._is_gpu_available = test.is_gpu_available()
if cls._is_gpu_available:
    gpu_name = test_util.gpu_device_name()
    cls._main_device = "/job:localhost/replica:0/task:0" + gpu_name
else:
    cls._main_device = "/job:localhost/replica:0/task:0/device:CPU:0"

with session.Session(config=no_rewrite_session_config()) as sess:
    x_init_val = np.array([5.0, 3.0])
    x_init = constant_op.constant(x_init_val, shape=[2])
    x = variables.VariableV1(x_init, name="control_deps/x")

    y = math_ops.add(x, x, name="control_deps/y")
    y = control_flow_ops.with_dependencies(
        [x], y, name="control_deps/ctrl_dep_y")

    z = math_ops.multiply(x, y, name="control_deps/z")

    z = control_flow_ops.with_dependencies(
        [x, y], z, name="control_deps/ctrl_dep_z")

    x.initializer.run()

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls="file://%s" % cls._dump_root)

    # Invoke Session.run().
    run_metadata = config_pb2.RunMetadata()
    sess.run(z, options=run_options, run_metadata=run_metadata)

debug_dump = debug_data.DebugDumpDir(
    cls._dump_root, partition_graphs=run_metadata.partition_graphs)

# Construct the analyzer and command handler registry.
_, cls._registry = create_analyzer_cli(debug_dump)
