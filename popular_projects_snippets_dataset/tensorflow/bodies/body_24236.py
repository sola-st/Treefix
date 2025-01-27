# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)
v = variables.VariableV1(42)
tensor_runner = wrapped_sess.make_callable(v)
self.sess.run(v.initializer)

self.assertAllClose(42, tensor_runner())
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))
