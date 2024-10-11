# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
op_namespace = "testDumpUninitializedVariable"
with session.Session() as sess:
    u_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
    s_init_val = b"str1"

    u_name = "%s/u" % op_namespace
    s_name = "%s/s" % op_namespace

    u_init = constant_op.constant(u_init_val, shape=[2, 2])
    u = variables.VariableV1(u_init, name=u_name)
    s_init = constant_op.constant(s_init_val)
    s = variables.VariableV1(s_init, name=s_name)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_urls = self._debug_urls()

    # Add debug tensor watch for u.
    debug_utils.add_debug_tensor_watch(
        run_options, u_name, 0, debug_urls=debug_urls)
    debug_utils.add_debug_tensor_watch(
        run_options, s_name, 0, debug_urls=debug_urls)

    run_metadata = config_pb2.RunMetadata()

    # Initialize u and s.
    sess.run(variables.global_variables_initializer(),
             options=run_options,
             run_metadata=run_metadata)

    # Verify the dump file for the uninitialized value of u.
    dump = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)

    self.assertEqual(2, dump.size)
    self.assertEqual(self._expected_partition_graph_count,
                     len(run_metadata.partition_graphs))

    # Verify that the variable is properly initialized by the run() call.
    u_vals = dump.get_tensors(u_name, 0, "DebugIdentity")
    s_vals = dump.get_tensors(s_name, 0, "DebugIdentity")
    self.assertEqual(1, len(u_vals))
    self.assertIsInstance(u_vals[0], debug_data.InconvertibleTensorProto)
    self.assertFalse(u_vals[0].initialized)
    self.assertEqual(1, len(s_vals))
    self.assertIsInstance(s_vals[0], debug_data.InconvertibleTensorProto)
    self.assertFalse(s_vals[0].initialized)

    # Call run() again, to check that u is initialized properly.
    self.assertAllClose(u_init_val, sess.run(u))
    self.assertEqual(s_init_val, sess.run(s))
