# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/max_pool_with_argmax.py
values = [
    create_tensor_data(
        tf.float32, parameters['input_size'], min_value=-10, max_value=10)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
