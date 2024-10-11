# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)

# Do a run that should lead to an TensorFlow runtime error.
wrapped_sess.run(self.y, feed_dict={self.ph: [[0.0], [1.0], [2.0]]})

self.assertEqual([1], wrapped_sess.observers["run_start_cli_run_numbers"])
self.assertEqual([1], wrapped_sess.observers["run_end_cli_run_numbers"])
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))

# Verify that the runtime error is caught by the wrapped session properly.
self.assertEqual(1, len(wrapped_sess.observers["tf_errors"]))
tf_error = wrapped_sess.observers["tf_errors"][0]
self.assertEqual("y", tf_error.op.name)
