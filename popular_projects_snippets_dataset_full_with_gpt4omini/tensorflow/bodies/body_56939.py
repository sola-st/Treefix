# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/one_hot.py
"""Build the input for one_hot op."""
input_values = [
    create_tensor_data(
        parameters["indices_type"],
        shape=parameters["indices_shape"],
        min_value=-1,
        max_value=10),
    create_tensor_data(tf.int32, shape=None, min_value=1, max_value=10),
]

if parameters["provide_optional_inputs"]:
    input_values.append(
        create_tensor_data(
            parameters["dtype"], shape=None, min_value=1, max_value=10))
    input_values.append(
        create_tensor_data(
            parameters["dtype"], shape=None, min_value=-1, max_value=0))

exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
