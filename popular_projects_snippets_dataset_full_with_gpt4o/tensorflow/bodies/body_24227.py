# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"], ["run"]], self.sess, dump_root=self._tmp_dir)

# run under debug mode twice.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

# Verify that the assign_add op did take effect.
self.assertAllClose(12.0, self.sess.run(self.v))

# Assert correct run call numbers for which the CLI has been launched at
# run-start and run-end.
self.assertEqual([1], wrapped_sess.observers["run_start_cli_run_numbers"])
self.assertEqual([1, 2], wrapped_sess.observers["run_end_cli_run_numbers"])

# Verify that the dumps have been generated and picked up during run-end.
self.assertEqual(2, len(wrapped_sess.observers["debug_dumps"]))

# Verify that the TensorFlow runtime errors are picked up and in this case,
# they should be both None.
self.assertEqual([None, None], wrapped_sess.observers["tf_errors"])
