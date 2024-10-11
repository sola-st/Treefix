# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/placeholder_with_default.py
numpy_type = MAP_TF_TO_NUMPY_TYPE[parameters["dtype"]]
input_value = np.array([[1, 0], [2, 1]], numpy_type)
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
