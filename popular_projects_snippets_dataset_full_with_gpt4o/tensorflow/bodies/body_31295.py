# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep = array_ops.ones([])
res = self._testDropoutWrapper(
    input_keep_prob=keep, output_keep_prob=keep, state_keep_prob=keep,
    wrapper_type=wrapper_type)
true_full_output = np.array(
    [[[0.751109, 0.751109, 0.751109]], [[0.895509, 0.895509, 0.895509]]],
    dtype=np.float32)
true_full_final_c = np.array(
    [[1.949385, 1.949385, 1.949385]], dtype=np.float32)
self.assertAllClose(true_full_output, res[0])
self.assertAllClose(true_full_output[1], res[1].h)
self.assertAllClose(true_full_final_c, res[1].c)
