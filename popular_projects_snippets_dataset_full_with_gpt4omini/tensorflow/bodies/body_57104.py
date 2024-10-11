# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/local_response_norm.py
input_values = create_tensor_data(
    np.float32, parameters["input_shape"], min_value=-4, max_value=10)
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
