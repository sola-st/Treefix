# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session():
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
        cell(x, m)  # Execute to create variables
    variables = variables_lib.global_variables()
    self.assertEqual(variables[0].op.name, "root/lstm_cell/kernel")
    self.assertEqual(variables[1].op.name, "root/lstm_cell/bias")
    self.assertEqual(variables[2].op.name, "root/lstm_cell/projection/kernel")
