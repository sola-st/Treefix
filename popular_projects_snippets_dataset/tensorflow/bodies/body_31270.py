# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
"""Tests that state_size must be num_units * 2."""
with self.cached_session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        num_units = 2
        state_size = num_units * 3  # state_size must be num_units * 2
        batch_size = 3
        input_size = 4
        x = array_ops.zeros([batch_size, input_size])
        m = array_ops.zeros([batch_size, state_size])
        with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
            g, out_m = rnn_cell_impl.BasicLSTMCell(
                num_units, state_is_tuple=False)(x, m)
            sess.run([variables_lib.global_variables_initializer()])
            sess.run(
                [g, out_m], {
                    x: 1 * np.ones([batch_size, input_size]),
                    m: 0.1 * np.ones([batch_size, state_size])
                })
