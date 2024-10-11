# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-n"], ["run", "-n"], ["run", "-n"]],
    self.sess, dump_root=self._tmp_dir)

# run three times.
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)
wrapped_sess.run(self.inc_v)

self.assertAllClose(13.0, self.sess.run(self.v))

self.assertEqual([1, 2, 3],
                 wrapped_sess.observers["run_start_cli_run_numbers"])
self.assertEqual([], wrapped_sess.observers["run_end_cli_run_numbers"])
