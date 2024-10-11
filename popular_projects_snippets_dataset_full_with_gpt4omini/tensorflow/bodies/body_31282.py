# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        x = array_ops.zeros([1, 2])
        m = array_ops.zeros([1, 4])
        multi_rnn_cell = rnn_cell_impl.MultiRNNCell(
            [rnn_cell_impl.GRUCell(2) for _ in range(2)],
            state_is_tuple=False)
        _, ml = multi_rnn_cell(x, m)
        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run(ml, {
            x: np.array([[1., 1.]]),
            m: np.array([[0.1, 0.1, 0.1, 0.1]])
        })
        # The numbers in results were not calculated, this is just a smoke test.
        self.assertAllClose(res, [[0.175991, 0.175991, 0.13248, 0.13248]])
        self.assertEqual(len(multi_rnn_cell.weights), 2 * 4)
        self.assertTrue(
            [x.dtype == dtypes.float32 for x in multi_rnn_cell.weights])
