# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/random_standard_normal.py
input_value = create_tensor_data(
    parameters["input_dtype"],
    parameters["input_shape"],
    min_value=1,
    max_value=10)
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
