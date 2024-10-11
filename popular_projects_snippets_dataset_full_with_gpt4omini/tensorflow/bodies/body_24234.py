# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-t", "3"]], self.sess, dump_root=self._tmp_dir)

# run twice, which is less than the number of times specified by the
# command.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(12.0, self.sess.run(self.v))

self.assertEqual([1], wrapped_sess.observers["run_start_cli_run_numbers"])
self.assertEqual([], wrapped_sess.observers["run_end_cli_run_numbers"])
self.assertEqual(0, len(wrapped_sess.observers["debug_dumps"]))
self.assertEqual([], wrapped_sess.observers["tf_errors"])
