# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
cls._dump_root = tempfile.mkdtemp()
cls._dump_root_for_unique = tempfile.mkdtemp()

cls._is_gpu_available = test.is_gpu_available()
if cls._is_gpu_available:
    gpu_name = test_util.gpu_device_name()
    cls._main_device = "/job:localhost/replica:0/task:0" + gpu_name
else:
    cls._main_device = "/job:localhost/replica:0/task:0/device:CPU:0"

cls._curr_file_path = os.path.abspath(
    tf_inspect.getfile(tf_inspect.currentframe()))

cls._sess = session.Session(config=no_rewrite_session_config())
with cls._sess as sess:
    u_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
    v_init_val = np.array([[2.0], [-1.0]])

    u_name = "simple_mul_add/u"
    v_name = "simple_mul_add/v"

    u_init = constant_op.constant(u_init_val, shape=[2, 2], name="u_init")
    u = variables.VariableV1(u_init, name=u_name)
    cls._u_line_number = line_number_above()

    v_init = constant_op.constant(v_init_val, shape=[2, 1], name="v_init")
    v = variables.VariableV1(v_init, name=v_name)
    cls._v_line_number = line_number_above()

    w = math_ops.matmul(u, v, name="simple_mul_add/matmul")
    cls._w_line_number = line_number_above()

    x = math_ops.add(w, w, name="simple_mul_add/add")
    cls._x_line_number = line_number_above()

    a = variables.VariableV1([1, 3, 3, 7], name="a")

    u.initializer.run()
    v.initializer.run()
    a.initializer.run()

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls="file://%s" % cls._dump_root)

    # Invoke Session.run().
    run_metadata = config_pb2.RunMetadata()
    sess.run([x], options=run_options, run_metadata=run_metadata)
    cls._debug_dump = debug_data.DebugDumpDir(
        cls._dump_root, partition_graphs=run_metadata.partition_graphs)
    cls._analyzer, cls._registry = create_analyzer_cli(cls._debug_dump)
