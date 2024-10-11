# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_some = 0.9
res = self._testDropoutWrapper(
    input_keep_prob=keep_some,
    output_keep_prob=keep_some,
    state_keep_prob=keep_some,
    variational_recurrent=True,
    wrapper_type=wrapper_type,
    input_size=3,
    batch_size=5,
    time_steps=7)

# Smoke test for the state/input masks.
output_mask = np.abs(res[0]) > 1e-6
for time_step in output_mask:
    # Ensure the same dropout output pattern for all time steps
    self.assertAllClose(output_mask[0], time_step)
    for batch_entry in time_step:
        # Assert all batch entries get the same mask
        self.assertAllClose(batch_entry, time_step[0])

    # For state, ensure all batch entries have the same mask
state_c_mask = np.abs(res[1].c) > 1e-6
state_h_mask = np.abs(res[1].h) > 1e-6
for batch_entry in state_c_mask:
    self.assertAllClose(batch_entry, state_c_mask[0])
for batch_entry in state_h_mask:
    self.assertAllClose(batch_entry, state_h_mask[0])
