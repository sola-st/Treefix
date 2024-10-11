# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/abs.py
min_value, max_value = (-10, 10)
if "input_range" in parameters:
    min_value, max_value = parameters["input_range"]
input_values = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=min_value,
    max_value=max_value)
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
