# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cond.py
input_values = [
    create_tensor_data(parameters["dtype"], (1,)),
    create_tensor_data(parameters["dtype"], (1,)),
    np.array([parameters["pred"]], dtype=np.bool_),
]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
