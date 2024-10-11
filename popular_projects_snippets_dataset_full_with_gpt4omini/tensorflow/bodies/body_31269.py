# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
"""Tests that dimension 0 in both(x and m) shape must be equal."""
with self.cached_session() as sess:
    with variable_scope.variable_scope(
        "root", initializer=init_ops.constant_initializer(0.5)):
        num_units = 2
        state_size = num_units * 2
        batch_size = 3
        input_size = 4
        x = array_ops.zeros([batch_size, input_size])
        m = array_ops.zeros([batch_size - 1, state_size])
        with self.assertRaises(ValueError):
            g, out_m = rnn_cell_impl.BasicLSTMCell(
                num_units, state_is_tuple=False)(x, m)
            sess.run([variables_lib.global_variables_initializer()])
            sess.run(
                [g, out_m], {
                    x: 1 * np.ones([batch_size, input_size]),
                    m: 0.1 * np.ones([batch_size - 1, state_size])
                })
