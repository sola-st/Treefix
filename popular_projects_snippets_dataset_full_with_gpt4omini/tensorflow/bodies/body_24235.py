# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-n"], ["run", "-t", "2"], ["run"], ["run"]],
    self.sess, dump_root=self._tmp_dir)

# run four times.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(14.0, self.sess.run(self.v))

self.assertEqual([1, 2],
                 wrapped_sess.observers["run_start_cli_run_numbers"])
self.assertEqual([3, 4], wrapped_sess.observers["run_end_cli_run_numbers"])
self.assertEqual(2, len(wrapped_sess.observers["debug_dumps"]))
self.assertEqual([None, None], wrapped_sess.observers["tf_errors"])
