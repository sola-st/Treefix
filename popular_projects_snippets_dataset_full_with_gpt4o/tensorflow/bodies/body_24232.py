# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
# Do two NON_DEBUG_RUNs, followed by DEBUG_RUNs.
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-n"], ["run", "-n"], ["run"], ["run"]],
    self.sess, dump_root=self._tmp_dir)

# run three times.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(13.0, self.sess.run(self.v))

self.assertEqual([1, 2, 3],
                 wrapped_sess.observers["run_start_cli_run_numbers"])

# Here, the CLI should have been launched only under the third run,
# because the first and second runs are NON_DEBUG.
self.assertEqual([3], wrapped_sess.observers["run_end_cli_run_numbers"])
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))
self.assertEqual([None], wrapped_sess.observers["tf_errors"])
