# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    str1_init_val = np.array(b"abc")
    str2_init_val = np.array(b"def")

    str1_init = constant_op.constant(str1_init_val)
    str2_init = constant_op.constant(str2_init_val)

    str1_name = "str1"
    str2_name = "str2"
    str1 = variables.VariableV1(str1_init, name=str1_name)
    str2 = variables.VariableV1(str2_init, name=str2_name)
    # Concatenate str1 and str2
    str_concat = math_ops.add(str1, str2, name="str_concat")

    str1.initializer.run()
    str2.initializer.run()

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_urls = self._debug_urls()

    # Add debug tensor watch for u.
    debug_utils.add_debug_tensor_watch(
        run_options, "%s/read" % str1_name, 0, debug_urls=debug_urls)
    # Add debug tensor watch for v.
    debug_utils.add_debug_tensor_watch(
        run_options, "%s/read" % str2_name, 0, debug_urls=debug_urls)

    run_metadata = config_pb2.RunMetadata()
    sess.run(str_concat, options=run_options, run_metadata=run_metadata)

    # String ops are located on CPU.
    self.assertEqual(1, len(run_metadata.partition_graphs))

    dump = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)

    self.assertIn(str1_name, dump.nodes())
    self.assertIn(str2_name, dump.nodes())

    self.assertEqual(2, dump.size)

    self.assertEqual([str1_init_val],
                     dump.get_tensors("%s/read" % str1_name, 0,
                                      "DebugIdentity"))
    self.assertEqual([str2_init_val],
                     dump.get_tensors("%s/read" % str2_name, 0,
                                      "DebugIdentity"))

    self.assertGreaterEqual(
        dump.get_rel_timestamps("%s/read" % str1_name, 0, "DebugIdentity")[0],
        0)
    self.assertGreaterEqual(
        dump.get_rel_timestamps("%s/read" % str2_name, 0, "DebugIdentity")[0],
        0)

    self.assertGreater(
        dump.get_dump_sizes_bytes("%s/read" % str1_name, 0,
                                  "DebugIdentity")[0], 0)
    self.assertGreater(
        dump.get_dump_sizes_bytes("%s/read" % str2_name, 0,
                                  "DebugIdentity")[0], 0)
