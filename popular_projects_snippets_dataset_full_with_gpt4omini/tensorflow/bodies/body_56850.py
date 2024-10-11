# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_to.py
input_values = [
    create_tensor_data(parameters["input_dtype"], parameters["input_shape"])
]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
