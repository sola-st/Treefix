# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
(_, input_size) = inputs_list_t[0].get_shape().as_list()
initializer = init_ops.random_uniform_initializer(-0.01, 0.01, seed=127)
cell = rnn_cell_impl.LSTMCell(
    num_units=input_size,
    use_peepholes=True,
    initializer=initializer,
    state_is_tuple=False)
outputs, final_state = rnn.static_rnn(
    cell,
    inputs_list_t,
    sequence_length=sequence_length,
    dtype=dtypes.float32)

trainable_variables = ops_lib.get_collection(
    ops_lib.GraphKeys.TRAINABLE_VARIABLES)
gradients = gradients_impl.gradients(outputs + [final_state],
                                     trainable_variables)

exit(control_flow_ops.group(final_state, *(gradients + outputs)))
