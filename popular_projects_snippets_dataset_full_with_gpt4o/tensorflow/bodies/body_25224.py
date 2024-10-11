# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
cls._dump_root = tempfile.mkdtemp()

with session.Session(config=no_rewrite_session_config()) as sess:
    # 2400 elements should exceed the default threshold (2000).
    x = constant_op.constant(np.zeros([300, 8]), name="large_tensors/x")

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls="file://%s" % cls._dump_root)

    # Invoke Session.run().
    run_metadata = config_pb2.RunMetadata()
    sess.run(x, options=run_options, run_metadata=run_metadata)

cls._debug_dump = debug_data.DebugDumpDir(
    cls._dump_root, partition_graphs=run_metadata.partition_graphs)

# Construct the analyzer and command registry.
cls._analyzer, cls._registry = create_analyzer_cli(cls._debug_dump)
