# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
variable_1 = variables.VariableV1(
    10.5, dtype=dtypes.float32, name="variable_1")
a = math_ops.add(variable_1, variable_1, "callable_a")
math_ops.add(a, a, "callable_b")
self.sess.run(variable_1.initializer)

wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"]] * 3, self.sess, dump_root=self._tmp_dir)
callable_options = config_pb2.CallableOptions()
callable_options.fetch.append("callable_b")
sess_callable = wrapped_sess._make_callable_from_options(callable_options)

for _ in range(2):
    callable_output = sess_callable()
    self.assertAllClose(np.array(42.0, dtype=np.float32), callable_output[0])

debug_dumps = wrapped_sess.observers["debug_dumps"]
self.assertEqual(2, len(debug_dumps))
for debug_dump in debug_dumps:
    node_names = [datum.node_name for datum in debug_dump.dumped_tensor_data]
    self.assertItemsEqual(
        ["callable_a", "callable_b", "variable_1", "variable_1/read"],
        node_names)
