# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_all = variable_scope.get_variable("all", initializer=1.0)
keep_none = variable_scope.get_variable("none", initializer=1e-6)
res = self._testDropoutWrapper(
    input_keep_prob=keep_all,
    output_keep_prob=keep_none,
    state_keep_prob=keep_all,
    wrapper_type=wrapper_type)
true_full_output = np.array(
    [[[0.751109, 0.751109, 0.751109]], [[0.895509, 0.895509, 0.895509]]],
    dtype=np.float32)
true_full_final_c = np.array(
    [[1.949385, 1.949385, 1.949385]], dtype=np.float32)
self.assertAllClose(np.zeros(res[0].shape), res[0])
self.assertAllClose(true_full_output[1], res[1].h)
self.assertAllClose(true_full_final_c, res[1].c)
