# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unfused_gru.py
"""Build the inputs for unfused_gru."""
input_values = [
    create_tensor_data(tf.float32,
                       [parameters["batch_size"], parameters["units"]])
    for _ in range(parameters["time"])
]
init = tf.compat.v1.global_variables_initializer()
sess.run(init)
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
