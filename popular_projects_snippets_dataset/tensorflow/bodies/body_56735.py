# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/segment_sum.py
data = create_tensor_data(parameters["data_dtype"],
                          parameters["data_shape"])
exit(([data], sess.run(outputs, feed_dict=dict(zip(inputs, [data])))))
