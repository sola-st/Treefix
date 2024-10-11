# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "-p"], ["run"]], self.sess)

wrapped_sess.run(self.w_int)

self.assertEqual(1, len(wrapped_sess.observers["profiler_run_metadata"]))
self.assertTrue(
    wrapped_sess.observers["profiler_run_metadata"][0].step_stats)
self.assertEqual(1, len(wrapped_sess.observers["profiler_py_graphs"]))
self.assertIsInstance(
    wrapped_sess.observers["profiler_py_graphs"][0], ops.Graph)
