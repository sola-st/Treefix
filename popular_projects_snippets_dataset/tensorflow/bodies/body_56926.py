# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/relu6.py
min_value, max_value = parameters["input_range"]
input_values = create_tensor_data(np.float32, parameters["input_shape"],
                                  min_value, max_value)
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
