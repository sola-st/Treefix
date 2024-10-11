# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/constant.py
dummy_input = np.zeros(
    parameters["input_shape"],
    dtype=MAP_TF_TO_NUMPY_TYPE[parameters["dtype"]])
exit(([dummy_input], sess.run(outputs, feed_dict={inputs[0]: dummy_input})))
