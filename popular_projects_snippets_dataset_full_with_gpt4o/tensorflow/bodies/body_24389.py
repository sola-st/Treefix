# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
results = self._generate_dump_from_simple_addition_graph()
self.assertTrue(results.dump.loaded_partition_graphs())

# Since global_step is not explicitly specified, it should take its default
# value: -1.
self.assertEqual(-1, results.dump.core_metadata.global_step)
self.assertGreaterEqual(results.dump.core_metadata.session_run_index, 0)
self.assertGreaterEqual(results.dump.core_metadata.executor_step_index, 0)
self.assertEqual([], results.dump.core_metadata.input_names)
self.assertEqual([results.w.name], results.dump.core_metadata.output_names)
self.assertEqual([], results.dump.core_metadata.target_nodes)

# Verify the dumped tensor values for u and v.
self.assertEqual(2, results.dump.size)

self.assertAllClose([results.u_init_val],
                    results.dump.get_tensors("%s/read" % results.u_name, 0,
                                             "DebugIdentity"))
self.assertAllClose([results.v_init_val],
                    results.dump.get_tensors("%s/read" % results.v_name, 0,
                                             "DebugIdentity"))

self.assertGreaterEqual(
    results.dump.get_rel_timestamps("%s/read" % results.u_name, 0,
                                    "DebugIdentity")[0], 0)
self.assertGreaterEqual(
    results.dump.get_rel_timestamps("%s/read" % results.v_name, 0,
                                    "DebugIdentity")[0], 0)

self.assertGreater(
    results.dump.get_dump_sizes_bytes("%s/read" % results.u_name, 0,
                                      "DebugIdentity")[0], 0)
self.assertGreater(
    results.dump.get_dump_sizes_bytes("%s/read" % results.v_name, 0,
                                      "DebugIdentity")[0], 0)
