# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/splitv.py
values = [create_tensor_data(np.float32, parameters["input_shape"])]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
