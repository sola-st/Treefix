# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/zeros_like.py
values = create_tensor_data(parameters["input_dtype"],
                            parameters["input_shape"])
exit(([values], sess.run(outputs, feed_dict=dict(zip(inputs, [values])))))
