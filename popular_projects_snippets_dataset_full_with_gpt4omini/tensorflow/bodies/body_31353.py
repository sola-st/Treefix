# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
cell = cell_class(out_size, dtype=dtype)
in_shape = tensor_shape.TensorShape((batch_size, in_size))
cell.build(in_shape)
state_output = cell.get_initial_state(
    inputs=None, batch_size=batch_size, dtype=dtype)
cell_output, _ = cell(array_ops.zeros(in_shape, dtype), state_output)
self.assertAllEqual([batch_size, out_size], cell_output.shape.as_list())
