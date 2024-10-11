# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        x = array_ops.zeros([1, 2])
        m_bad = array_ops.zeros([1, 4])
        m_good = (array_ops.zeros([1, 2]), array_ops.zeros([1, 2]))

        # Test incorrectness of state
        with self.assertRaisesRegex(ValueError, "Expected state .* a tuple"):
            rnn_cell_impl.MultiRNNCell(
                [rnn_cell_impl.GRUCell(2) for _ in range(2)],
                state_is_tuple=True)(x, m_bad)

        _, ml = rnn_cell_impl.MultiRNNCell(
            [rnn_cell_impl.GRUCell(2) for _ in range(2)],
            state_is_tuple=True)(x, m_good)

        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run(
            ml, {
                x: np.array([[1., 1.]]),
                m_good[0]: np.array([[0.1, 0.1]]),
                m_good[1]: np.array([[0.1, 0.1]])
            })

        # The numbers in results were not calculated, this is just a
        # smoke test.  However, these numbers should match those of
        # the test testMultiRNNCell.
        self.assertAllClose(res[0], [[0.175991, 0.175991]])
        self.assertAllClose(res[1], [[0.13248, 0.13248]])
