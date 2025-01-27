# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    u_name = "testDumpCausalityCheck/u"
    v_name = "testDumpCausalityCheck/v"
    w_name = "testDumpCausalityCheck/w"

    u_init = constant_op.constant([2.0, 4.0])
    u = variables.VariableV1(u_init, name=u_name)
    v = math_ops.add(u, u, name=v_name)
    w = math_ops.add(v, v, name=w_name)

    u.initializer.run()

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls=self._debug_urls())

    run_metadata = config_pb2.RunMetadata()
    sess.run(w, options=run_options, run_metadata=run_metadata)

    self.assertEqual(self._expected_partition_graph_count,
                     len(run_metadata.partition_graphs))

    # First, loading the original dump without supplying the
    # partition_graphs should not cause a LookupError, validation occurs
    # only with partition_graphs loaded.
    debug_data.DebugDumpDir(self._dump_root)

    # Now, loading the original dump with partition graphs supplied should
    # succeed. The validation should pass quietly.
    dump = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)

    # Get the dump file names and compute their timestamps.
    self.assertEqual(
        1, len(dump.get_tensor_file_paths(v_name, 0, "DebugIdentity")))
    v_file_path = dump.get_tensor_file_paths(v_name, 0, "DebugIdentity")[0]

    self.assertEqual(
        1, len(dump.get_tensor_file_paths(w_name, 0, "DebugIdentity")))
    w_file_path = dump.get_tensor_file_paths(w_name, 0, "DebugIdentity")[0]

    v_timestamp = int(v_file_path[v_file_path.rindex("_") + 1:])
    w_timestamp = int(w_file_path[w_file_path.rindex("_") + 1:])

    # Swap and slightly shift the time stamps of the last two dumped tensors,
    # to simulate "causality violation", which can happen if the dump
    # directory contains incomplete data and/or mixes data from different
    # Session.run() calls.
    v_file_path_1 = v_file_path[:v_file_path.rindex(
        "_")] + "_%d" % w_timestamp
    w_file_path_1 = w_file_path[:w_file_path.rindex("_")] + "_%d" % (
        v_timestamp - 1)

    os.rename(v_file_path, v_file_path_1)
    os.rename(w_file_path, w_file_path_1)

    # Load the dump directory again. Now a ValueError is expected to be
    # raised due to the timestamp swap.
    with self.assertRaisesRegexp(ValueError, "Causality violated"):
        dump = debug_data.DebugDumpDir(
            self._dump_root, partition_graphs=run_metadata.partition_graphs)

    # Loading the dump directory with kwarg "validate" set explicitly to
    # False should get rid of the error.
    dump = debug_data.DebugDumpDir(
        self._dump_root,
        partition_graphs=run_metadata.partition_graphs,
        validate=False)

    # Next, set the two times stamps to be the same, which should be fine.
    v_file_path_2 = v_file_path[:v_file_path.rindex(
        "_")] + "_%d" % w_timestamp
    w_file_path_2 = w_file_path[:w_file_path.rindex(
        "_")] + "_%d" % w_timestamp

    os.rename(v_file_path_1, v_file_path_2)
    os.rename(w_file_path_1, w_file_path_2)

    debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)
