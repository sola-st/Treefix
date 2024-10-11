# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DeviceWrapper
x = array_ops.zeros([1, 3])
m = array_ops.zeros([1, 3])
cell = rnn_cell_impl.GRUCell(3)
wrapped_cell = wrapper_type(cell, "/cpu:0")
wrapped_cell.get_config()  # Should not throw an error
self.assertEqual(wrapped_cell._trackable_children()["cell"], cell)

outputs, _ = wrapped_cell(x, m)
self.assertIn("cpu:0", outputs.device.lower())
