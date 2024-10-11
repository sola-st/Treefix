# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run", "--op_type_filter", "Variable.*"],
     ["run", "--tensor_dtype_filter", "int32"],
     ["run"]],
    self.sess, dump_root=self._tmp_dir)

# run under debug mode twice.
wrapped_sess.run(self.w_int)
wrapped_sess.run(self.w_int)

# Verify that the dumps have been generated and picked up during run-end.
self.assertEqual(2, len(wrapped_sess.observers["debug_dumps"]))

dumps = wrapped_sess.observers["debug_dumps"][0]
self.assertEqual(2, dumps.size)
self.assertItemsEqual(
    ["v", "w"], [dumps.dumped_tensor_data[i].node_name for i in [0, 1]])

dumps = wrapped_sess.observers["debug_dumps"][1]
self.assertEqual(2, dumps.size)
self.assertEqual(
    ["w_int_inner", "w_int_outer"],
    [dumps.dumped_tensor_data[i].node_name for i in [0, 1]])
