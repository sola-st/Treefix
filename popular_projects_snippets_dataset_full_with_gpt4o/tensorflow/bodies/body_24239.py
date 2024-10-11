# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)
ph1 = array_ops.placeholder(dtypes.float32)
ph2 = array_ops.placeholder(dtypes.float32)
a = math_ops.add(ph1, ph2)
tensor_runner = wrapped_sess.make_callable(a, feed_list=[ph1, ph2])

self.assertAllClose(42.0, tensor_runner(41.0, 1.0))
self.assertEqual(1, len(wrapped_sess.observers["debug_dumps"]))
