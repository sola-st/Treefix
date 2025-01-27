# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_all = variable_scope.get_variable("all", initializer=1.0)
keep_none = variable_scope.get_variable("none", initializer=1e-6)
# Even though we dropout state, by default DropoutWrapper never
# drops out the memory ("c") term of an LSTMStateTuple.
res = self._testDropoutWrapper(
    input_keep_prob=keep_all,
    output_keep_prob=keep_all,
    state_keep_prob=keep_none,
    wrapper_type=wrapper_type)
true_c_state = np.array([[1.713925, 1.713925, 1.713925]], dtype=np.float32)
true_full_output = np.array(
    [[[0.751109, 0.751109, 0.751109]], [[0.895509, 0.895509, 0.895509]]],
    dtype=np.float32)
self.assertAllClose(true_full_output[0], res[0][0])
# Second output is modified by zero input state
self.assertGreater(np.linalg.norm(true_full_output[1] - res[0][1]), 1e-4)
# h state has been set to zero
self.assertAllClose(np.zeros(res[1].h.shape), res[1].h)
# c state of an LSTMStateTuple is NEVER modified.
self.assertAllClose(true_c_state, res[1].c)
