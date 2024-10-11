# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
data_value = create_tensor_data(
    parameters["dtype"], shape=parameters["data_shape"])
exit(([data_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [data_value])))))
