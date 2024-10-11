# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_all = variable_scope.get_variable("all", initializer=1.0)
keep_none = variable_scope.get_variable("none", initializer=1e-6)
true_full_output = np.array(
    [[[0.751109, 0.751109, 0.751109]], [[0.895509, 0.895509, 0.895509]]],
    dtype=np.float32)
true_full_final_c = np.array(
    [[1.949385, 1.949385, 1.949385]], dtype=np.float32)
# All outputs are different because inputs are zeroed out
res = self._testDropoutWrapper(
    input_keep_prob=keep_none,
    output_keep_prob=keep_all,
    state_keep_prob=keep_all,
    wrapper_type=wrapper_type)
self.assertGreater(np.linalg.norm(res[0] - true_full_output), 1e-4)
self.assertGreater(np.linalg.norm(res[1].h - true_full_output[1]), 1e-4)
self.assertGreater(np.linalg.norm(res[1].c - true_full_final_c), 1e-4)
