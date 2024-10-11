# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unpack.py
input_value = create_tensor_data(
    parameters["dtype"], shape=parameters["base_shape"])
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
