# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_some = 0.8
keep_all = variable_scope.get_variable("all", initializer=1.0)
res = self._testDropoutWrapper(
    input_keep_prob=keep_all,
    output_keep_prob=keep_some,
    state_keep_prob=keep_all,
    variational_recurrent=True,
    wrapper_type=wrapper_type,
    input_size=3,
    batch_size=5,
    time_steps=7)
# Ensure the same dropout pattern for all time steps
output_mask = np.abs(res[0]) > 1e-6
for m in output_mask[1:]:
    self.assertAllClose(output_mask[0], m)
