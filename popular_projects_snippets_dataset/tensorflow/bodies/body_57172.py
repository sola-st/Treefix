# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/control_dep.py
input_values = create_tensor_data(tf.float32, parameters["input_shape"])
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
