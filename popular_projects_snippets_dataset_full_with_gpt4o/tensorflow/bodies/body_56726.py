# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/while_loop.py
numpy_type = zip_test_utils.MAP_TF_TO_NUMPY_TYPE[parameters["dtype"]]
input_values = [
    np.array([parameters["num_iterations"]], dtype=np.int32),
    np.array(parameters["increment_value"], dtype=numpy_type)
]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
