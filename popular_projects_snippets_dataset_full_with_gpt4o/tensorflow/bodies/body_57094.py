# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/nearest_upsample.py
input_values = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=-10,
    max_value=10)
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
