# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/depth_to_space.py
if not parameters["fully_quantize"]:
    input_values = create_tensor_data(parameters["dtype"],
                                      parameters["input_shape"])
else:
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
