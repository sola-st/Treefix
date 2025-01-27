# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_with_constant.py
reference_values = np.zeros(parameters["reference_shape"], dtype=np.int32)
exit(([reference_values], sess.run(
    outputs, feed_dict={inputs[0]: reference_values})))
