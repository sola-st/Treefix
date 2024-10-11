# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sign.py
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
exit(([input_value], sess.run(outputs, dict(zip(inputs, [input_value])))))
