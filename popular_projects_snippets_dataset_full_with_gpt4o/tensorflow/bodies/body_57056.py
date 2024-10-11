# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fill.py
input1 = create_tensor_data(parameters["dims_dtype"],
                            parameters["dims_shape"], 1)
input2 = create_scalar_data(parameters["value_dtype"])
exit(([input1, input2], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input1, input2])))))
