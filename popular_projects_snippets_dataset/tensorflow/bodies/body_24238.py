# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)
v = variables.VariableV1(10.0)
inc_v = state_ops.assign_add(v, 1.0)
op_runner = wrapped_sess.make_callable(inc_v.op)
self.sess.run(v.initializer)

op_runner()
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))
self.assertEqual(11.0, self.sess.run(v))
