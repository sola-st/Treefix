# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/resolve_constant_strided_slice.py
del parameters
input_values = np.zeros([4, 2], dtype=np.float32)
exit(([input_values], sess.run(
    outputs, feed_dict={inputs[0]: input_values})))
