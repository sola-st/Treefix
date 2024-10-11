# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
if test.is_gpu_available():
    self.skipTest("No testing concurrent runs on a single GPU.")

with session.Session() as sess:
    v = variables.VariableV1(30.0, name="v")
    constants = []
    for i in range(self._num_concurrent_runs):
        constants.append(constant_op.constant(1.0, name="c%d" % i))
    incs = [
        state_ops.assign_add(
            v, c, use_locking=True, name=("inc%d" % i))
        for (i, c) in enumerate(constants)
    ]
    sess.run(v.initializer)

    concurrent_debug_urls = self._get_concurrent_debug_urls()

    def inc_job(index):
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        debug_utils.watch_graph(
            run_options, sess.graph, debug_urls=concurrent_debug_urls[index])
        for _ in range(100):
            sess.run(incs[index], options=run_options)

    inc_threads = []
    for index in range(self._num_concurrent_runs):
        inc_thread = threading.Thread(target=functools.partial(inc_job, index))
        inc_thread.start()
        inc_threads.append(inc_thread)
    for inc_thread in inc_threads:
        inc_thread.join()

    self.assertAllClose(30.0 + 1.0 * self._num_concurrent_runs * 100,
                        sess.run(v))

    all_session_run_indices = []
    for index in range(self._num_concurrent_runs):
        dump = debug_data.DebugDumpDir(self._dump_roots[index])
        self.assertTrue(dump.loaded_partition_graphs())

        v_data = dump.get_tensors("v", 0, "DebugIdentity")
        self.assertEqual(100, len(v_data))

        # Examine all the core metadata files
        core_metadata_files = glob.glob(
            os.path.join(self._dump_roots[index], "_tfdbg_core*"))

        timestamps = []
        session_run_indices = []
        executor_step_indices = []
        for core_metadata_file in core_metadata_files:
            with open(core_metadata_file, "rb") as f:
                event = event_pb2.Event()
                event.ParseFromString(f.read())
                core_metadata = (
                    debug_data.extract_core_metadata_from_event_proto(event))
                timestamps.append(event.wall_time)
                session_run_indices.append(core_metadata.session_run_index)
                executor_step_indices.append(core_metadata.executor_step_index)

        all_session_run_indices.extend(session_run_indices)

        # Assert that executor_step_index increases by one at a time.
        executor_step_indices = zip(timestamps, executor_step_indices)
        executor_step_indices = sorted(
            executor_step_indices, key=lambda x: x[0])
        for i in range(len(executor_step_indices) - 1):
            self.assertEquals(executor_step_indices[i][1] + 1,
                              executor_step_indices[i + 1][1])

        # Assert that session_run_index increase monotonically.
        session_run_indices = zip(timestamps, session_run_indices)
        session_run_indices = sorted(session_run_indices, key=lambda x: x[0])
        for i in range(len(session_run_indices) - 1):
            self.assertGreater(session_run_indices[i + 1][1],
                               session_run_indices[i][1])

      # Assert that the session_run_indices from the concurrent run() calls are
      # all unique.
    self.assertEqual(len(all_session_run_indices),
                     len(set(all_session_run_indices)))
