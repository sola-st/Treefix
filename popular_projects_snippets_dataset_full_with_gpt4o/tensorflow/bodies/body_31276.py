# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.ResidualWrapper
x = ops.convert_to_tensor(np.array([[1., 1., 1.]]))
m = ops.convert_to_tensor(np.array([[0.1, 0.1, 0.1]]))
base_cell = rnn_cell_impl.GRUCell(
    3, kernel_initializer=init_ops.constant_initializer(0.5),
    bias_initializer=init_ops.constant_initializer(0.5))
g, m_new = base_cell(x, m)
wrapper_object = wrapper_type(base_cell)
wrapper_object.get_config()  # Should not throw an error

self.assertIn("cell", wrapper_object._trackable_children())
self.assertIs(wrapper_object._trackable_children()["cell"], base_cell)

g_res, m_new_res = wrapper_object(x, m)
self.evaluate([variables_lib.global_variables_initializer()])
res = self.evaluate([g, g_res, m_new, m_new_res])
# Residual connections
self.assertAllClose(res[1], res[0] + [1., 1., 1.])
# States are left untouched
self.assertAllClose(res[2], res[3])
