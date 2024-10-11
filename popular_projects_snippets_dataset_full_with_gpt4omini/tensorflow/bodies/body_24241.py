# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
ph1 = array_ops.placeholder(dtypes.float32, name="callable_ph1")
a = math_ops.add(ph1, ph1, "callable_a")
math_ops.add(a, a, "callable_b")

wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"]] * 3, self.sess, dump_root=self._tmp_dir)
callable_options = config_pb2.CallableOptions()
callable_options.feed.append("callable_ph1")
callable_options.fetch.append("callable_b")
sess_callable = wrapped_sess._make_callable_from_options(callable_options)

ph1_value = np.array([10.5, -10.5], dtype=np.float32)

for _ in range(2):
    callable_output = sess_callable(ph1_value)
    self.assertAllClose(
        np.array([42.0, -42.0], dtype=np.float32), callable_output[0])

debug_dumps = wrapped_sess.observers["debug_dumps"]
self.assertEqual(2, len(debug_dumps))
for debug_dump in debug_dumps:
    node_names = [datum.node_name for datum in debug_dump.dumped_tensor_data]
    self.assertIn("callable_a", node_names)
    self.assertIn("callable_b", node_names)
