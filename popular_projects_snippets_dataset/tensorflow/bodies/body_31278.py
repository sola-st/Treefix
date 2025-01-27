# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.ResidualWrapper
x = ops.convert_to_tensor(np.array([[1., 1., 1., 1., 1.]]))
m = ops.convert_to_tensor(np.array([[0.1, 0.1, 0.1]]))
base_cell = rnn_cell_impl.GRUCell(
    3, kernel_initializer=init_ops.constant_initializer(0.5),
    bias_initializer=init_ops.constant_initializer(0.5))
g, m_new = base_cell(x, m)

def residual_with_slice_fn(inp, out):
    inp_sliced = array_ops.slice(inp, [0, 0], [-1, 3])
    exit(inp_sliced + out)

g_res, m_new_res = wrapper_type(
    base_cell, residual_with_slice_fn)(x, m)
self.evaluate([variables_lib.global_variables_initializer()])
res_g, res_g_res, res_m_new, res_m_new_res = self.evaluate(
    [g, g_res, m_new, m_new_res])
# Residual connections
self.assertAllClose(res_g_res, res_g + [1., 1., 1.])
# States are left untouched
self.assertAllClose(res_m_new, res_m_new_res)
