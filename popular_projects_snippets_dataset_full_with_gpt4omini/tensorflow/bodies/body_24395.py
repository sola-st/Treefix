# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    num_iter = 10

    # "u" is the Variable being updated in the loop.
    u_name = "testDumpToFileWhileLoop/u"
    u_namespace = u_name.split("/")[0]

    u_init_val = np.array(11.0)
    u_init = constant_op.constant(u_init_val)
    u = variables.VariableV1(u_init, name=u_name)

    # "v" is the increment.
    v_name = "testDumpToFileWhileLoop/v"
    v_namespace = v_name.split("/")[0]

    v_init_val = np.array(2.0)
    v_init = constant_op.constant(v_init_val)
    v = variables.VariableV1(v_init, name=v_name)

    u.initializer.run()
    v.initializer.run()

    i = constant_op.constant(0, name="testDumpToFileWhileLoop/i")

    def cond(i):
        exit(math_ops.less(i, num_iter))

    def body(i):
        new_u = state_ops.assign_add(u, v)
        new_i = math_ops.add(i, 1)
        op = control_flow_ops.group(new_u)
        new_i = control_flow_ops.with_dependencies([op], new_i)
        exit([new_i])

    loop = control_flow_ops.while_loop(
        cond, body, [i], parallel_iterations=10)

    # Create RunOptions for debug-watching tensors
    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_urls = self._debug_urls()

    # Add debug tensor watch for u.
    debug_utils.add_debug_tensor_watch(
        run_options, u_name, 0, debug_urls=debug_urls)
    # Add debug tensor watch for v.
    debug_utils.add_debug_tensor_watch(
        run_options, "%s/read" % v_name, 0, debug_urls=debug_urls)
    # Add debug tensor watch for while/Identity.
    debug_utils.add_debug_tensor_watch(
        run_options, "while/Identity", 0, debug_urls=debug_urls)
    # Add debug tensor watch for while/Add/y.
    debug_utils.add_debug_tensor_watch(
        run_options, "while/Add/y", 0, debug_urls=debug_urls)

    run_metadata = config_pb2.RunMetadata()
    r = sess.run(loop, options=run_options, run_metadata=run_metadata)

    self.assertEqual(self._expected_partition_graph_count,
                     len(run_metadata.partition_graphs))

    self.assertEqual(num_iter, r)
    u_val_final = sess.run(u)
    self.assertAllClose(u_init_val + num_iter * v_init_val, u_val_final)

    # Verify dump files
    self.assertTrue(os.path.isdir(self._dump_root))

    u_glob_out = glob.glob(os.path.join(self._dump_root, "*", u_namespace))
    v_glob_out = glob.glob(os.path.join(
        self._dump_root, "*", v_namespace, "v"))
    self.assertTrue(os.path.isdir(u_glob_out[0]))
    self.assertTrue(os.path.isdir(v_glob_out[0]))

    dump = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)

    # Expected dumped tensors: u, v/read, 10 iterations of while/Identity,
    # and 10 iterations of while/Add/y.
    self.assertEqual(1 + 1 + num_iter + num_iter, dump.size)

    # Verify tensor values.
    self.assertAllClose([u_init_val],
                        dump.get_tensors(u_name, 0, "DebugIdentity"))
    self.assertAllClose([v_init_val],
                        dump.get_tensors("%s/read" % v_name, 0,
                                         "DebugIdentity"))

    while_id_tensors = dump.get_tensors("while/Identity", 0, "DebugIdentity")
    self.assertEqual(10, len(while_id_tensors))
    for k in range(len(while_id_tensors)):
        self.assertAllClose(np.array(k), while_id_tensors[k])

    # Verify ascending timestamps from the while loops.
    while_id_rel_timestamps = dump.get_rel_timestamps("while/Identity", 0,
                                                      "DebugIdentity")
    while_id_dump_sizes_bytes = dump.get_dump_sizes_bytes("while/Identity", 0,
                                                          "DebugIdentity")
    self.assertEqual(10, len(while_id_rel_timestamps))
    prev_rel_time = 0
    prev_dump_size_bytes = while_id_dump_sizes_bytes[0]
    for rel_time, dump_size_bytes in zip(while_id_rel_timestamps,
                                         while_id_dump_sizes_bytes):
        self.assertGreaterEqual(rel_time, prev_rel_time)
        self.assertEqual(dump_size_bytes, prev_dump_size_bytes)
        prev_rel_time = rel_time
        prev_dump_size_bytes = dump_size_bytes

    # Test querying debug watch keys from node name.
    watch_keys = dump.debug_watch_keys("while/Identity")
    self.assertEqual(["while/Identity:0:DebugIdentity"], watch_keys)

    # Test querying debug datum instances from debug watch key.
    self.assertEqual(10, len(dump.watch_key_to_data(watch_keys[0])))
    self.assertEqual([], dump.watch_key_to_data("foo"))
