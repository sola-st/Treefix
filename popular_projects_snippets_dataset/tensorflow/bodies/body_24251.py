# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "--node_name_filter", "inc.*"],
     ["run", "--node_name_filter", "delta"],
     ["run"]],
    self.sess, dump_root=self._tmp_dir)

# run under debug mode twice.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

# Verify that the assign_add op did take effect.
self.assertAllClose(12.0, self.sess.run(self.v))

# Verify that the dumps have been generated and picked up during run-end.
self.assertEqual(2, len(wrapped_sess.observers["debug_dumps"]))

dumps = wrapped_sess.observers["debug_dumps"][0]
self.assertEqual(1, dumps.size)
self.assertEqual("inc_v", dumps.dumped_tensor_data[0].node_name)

dumps = wrapped_sess.observers["debug_dumps"][1]
self.assertEqual(1, dumps.size)
self.assertEqual("delta", dumps.dumped_tensor_data[0].node_name)
