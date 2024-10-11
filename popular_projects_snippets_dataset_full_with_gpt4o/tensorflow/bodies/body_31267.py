# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        x = array_ops.zeros([1, 2])
        m = array_ops.zeros([1, 2])
        g, _ = rnn_cell_impl.GRUCell(2)(x, m)
        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run([g], {
            x: np.array([[1., 1.]]),
            m: np.array([[0.1, 0.1]])
        })
        # Smoke test
        self.assertAllClose(res[0], [[0.175991, 0.175991]])
    with variable_scope.variable_scope(
        "other", initializer=init_ops.constant_initializer(0.5)):
        # Test GRUCell with input_size != num_units.
        x = array_ops.zeros([1, 3])
        m = array_ops.zeros([1, 2])
        g, _ = rnn_cell_impl.GRUCell(2)(x, m)
        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run([g], {
            x: np.array([[1., 1., 1.]]),
            m: np.array([[0.1, 0.1]])
        })
        # Smoke test
        self.assertAllClose(res[0], [[0.156736, 0.156736]])
