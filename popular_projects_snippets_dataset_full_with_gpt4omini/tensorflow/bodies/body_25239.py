# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
cls._dump_root = tempfile.mkdtemp()

with session.Session(config=no_rewrite_session_config()) as sess:
    loop_var = constant_op.constant(0, name="while_loop_test/loop_var")
    cond = lambda loop_var: math_ops.less(loop_var, 10)
    body = lambda loop_var: math_ops.add(loop_var, 1)
    while_loop = control_flow_ops.while_loop(
        cond, body, [loop_var], parallel_iterations=1)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_url = "file://%s" % cls._dump_root

    watch_opts = run_options.debug_options.debug_tensor_watch_opts

    # Add debug tensor watch for "while/Identity".
    watch = watch_opts.add()
    watch.node_name = "while/Identity"
    watch.output_slot = 0
    watch.debug_ops.append("DebugIdentity")
    watch.debug_urls.append(debug_url)

    # Invoke Session.run().
    run_metadata = config_pb2.RunMetadata()
    sess.run(while_loop, options=run_options, run_metadata=run_metadata)

cls._debug_dump = debug_data.DebugDumpDir(
    cls._dump_root, partition_graphs=run_metadata.partition_graphs)

cls._analyzer, cls._registry = create_analyzer_cli(cls._debug_dump)
