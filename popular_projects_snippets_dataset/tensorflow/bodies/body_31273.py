# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session() as sess:
    num_units = 8
    num_proj = 6
    state_size = num_units + num_proj
    batch_size = 3
    input_size = 2
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        x = array_ops.zeros([batch_size, input_size])
        m = array_ops.zeros([batch_size, state_size])
        cell = rnn_cell_impl.LSTMCell(
            num_units=num_units,
            num_proj=num_proj,
            forget_bias=1.0,
            state_is_tuple=False)
        output, state = cell(x, m)
        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run(
            [output, state], {
                x: np.array([[1., 1.], [2., 2.], [3., 3.]]),
                m: 0.1 * np.ones((batch_size, state_size))
            })
        self.assertEqual(len(res), 2)
        # The numbers in results were not calculated, this is mostly just a
        # smoke test.
        self.assertEqual(res[0].shape, (batch_size, num_proj))
        self.assertEqual(res[1].shape, (batch_size, state_size))
        # Different inputs so different outputs and states
        for i in range(1, batch_size):
            self.assertTrue(
                float(np.linalg.norm((res[0][0, :] - res[0][i, :]))) > 1e-6)
            self.assertTrue(
                float(np.linalg.norm((res[1][0, :] - res[1][i, :]))) > 1e-6)
