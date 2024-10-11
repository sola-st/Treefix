# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/greater.py
input_value1 = create_tensor_data(parameters["input_dtype"],
                                  parameters["input_shape_pair"][0])
input_value2 = create_tensor_data(parameters["input_dtype"],
                                  parameters["input_shape_pair"][1])
exit(([input_value1, input_value2], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))
