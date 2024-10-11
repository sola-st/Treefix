# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool.py
if allow_fully_quantize:
    input_values = create_tensor_data(
        tf.float32, parameters["input_shape"], min_value=-1, max_value=1)
else:
    input_values = create_tensor_data(tf.float32, parameters["input_shape"])
exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))
