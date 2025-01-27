# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fused_batch_norm.py
# Fill dynamic shape with a random number.
input_shape = parameters["input_shape"]
input_shape = [
    np.random.randint(1, 10) if v is None else v for v in input_shape
]

input_values = [
    create_tensor_data(parameters["dtype"], input_shape),
    create_tensor_data(parameters["dtype"], input_shape)
]

exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
