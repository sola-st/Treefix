# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_rnn_with_control_flow_v2.py
"""Feed inputs, assign variables, and freeze graph."""

with tf.compat.v1.variable_scope("", reuse=True):
    kernel = tf.compat.v1.get_variable("rnn/basic_lstm_cell/kernel")
    bias = tf.compat.v1.get_variable("rnn/basic_lstm_cell/bias")
    kernel_values = create_tensor_data(parameters["dtype"],
                                       [kernel.shape[0], kernel.shape[1]], -1,
                                       1)
    bias_values = create_tensor_data(parameters["dtype"], [bias.shape[0]], 0,
                                     1)
    sess.run(tf.group(kernel.assign(kernel_values), bias.assign(bias_values)))

num_batches = parameters["num_batches"]
time_step_size = parameters["time_step_size"]
input_vec_size = parameters["input_vec_size"]
input_values = []
for _ in range(time_step_size):
    tensor_data = create_tensor_data(parameters["dtype"],
                                     [num_batches, input_vec_size], 0, 1)
    input_values.append(tensor_data)
out = sess.run(outputs, feed_dict=dict(zip(inputs, input_values)))
exit((input_values, out))
