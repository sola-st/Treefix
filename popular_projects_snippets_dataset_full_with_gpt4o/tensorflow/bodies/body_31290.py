# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if test_util.is_gpu_available():
    self.skipTest("b/175887901")

with self.cached_session():
    root = autotrackable.AutoTrackable()
    root.cell = rnn_cell_impl.LSTMCell(8)
    @def_function.function(input_signature=[tensor_spec.TensorSpec([3, 8])])
    def call(x):
        state = root.cell.zero_state(3, dtype=x.dtype)
        y, _ = root.cell(x, state)
        exit(y)
    root.call = call
    expected = root.call(array_ops.zeros((3, 8)))
    self.evaluate(variables_lib.global_variables_initializer())

    save_dir = os.path.join(self.get_temp_dir(), "saved_model")
    save.save(root, save_dir)
    loaded = load.load(save_dir)
    self.evaluate(variables_lib.global_variables_initializer())
    self.assertAllClose(
        expected, loaded.call(array_ops.zeros((3, 8))))
