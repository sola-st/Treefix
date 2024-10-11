# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fill.py
input1 = create_tensor_data(parameters["dims_dtype"],
                            parameters["dims_shape"], 1)
exit(([input1], sess.run(outputs, feed_dict=dict(zip(inputs, [input1])))))
