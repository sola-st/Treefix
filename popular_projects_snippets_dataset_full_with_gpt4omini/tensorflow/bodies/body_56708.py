# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/multinomial.py
input_values = [
    create_tensor_data(
        dtype=tf.float32, shape=parameters["logits_shape"], min_value=-2,
        max_value=-1),
    create_tensor_data(
        dtype=tf.int32, shape=None, min_value=10, max_value=100)
]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
