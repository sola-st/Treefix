# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
for wrapper_type in [
    rnn_cell_impl.DropoutWrapper,
    rnn_cell_impl.ResidualWrapper,
    lambda cell: rnn_cell_impl.MultiRNNCell([cell])]:
    cell = rnn_cell_impl.BasicRNNCell(1)
    wrapper = wrapper_type(cell)
    wrapper(array_ops.ones([1, 1]),
            state=wrapper.zero_state(batch_size=1, dtype=dtypes.float32))
    self.evaluate([v.initializer for v in cell.variables])
    checkpoint = trackable_utils.Checkpoint(wrapper=wrapper)
    prefix = os.path.join(self.get_temp_dir(), "ckpt")
    self.evaluate(cell._bias.assign([40.]))
    save_path = checkpoint.save(prefix)
    self.evaluate(cell._bias.assign([0.]))
    checkpoint.restore(save_path).assert_consumed().run_restore_ops()
    self.assertAllEqual([40.], self.evaluate(cell._bias))
