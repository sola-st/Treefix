# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_args.py
input_values = [
    np.array(parameters["input1_shape"]).astype(
        parameters["dtype"].as_numpy_dtype),
    np.array(parameters["input2_shape"]).astype(
        parameters["dtype"].as_numpy_dtype),
]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
