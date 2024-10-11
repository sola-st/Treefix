# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cast.py
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
