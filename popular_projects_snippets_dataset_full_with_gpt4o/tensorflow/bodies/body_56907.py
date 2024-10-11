# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/dynamic_rnn.py
"""Feed inputs, assign variables, and freeze graph."""
sess.run(tf.compat.v1.global_variables_initializer())

num_batches = parameters["num_batches"]
time_step_size = parameters["time_step_size"]
input_vec_size = parameters["input_vec_size"]
input_shape = (num_batches, time_step_size, input_vec_size)
input_value = create_tensor_data(parameters["dtype"], input_shape)

output_values = sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))
exit(([input_value], output_values))
