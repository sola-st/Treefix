# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/max_pool_with_argmax.py
"""Build the exp op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name='input', shape=parameters['input_size'])
updates, indices = tf.nn.max_pool_with_argmax(
    input_tensor,
    ksize=parameters['pool_size'],
    strides=parameters['strides'],
    padding=parameters['padding'],
    output_dtype=tf.dtypes.int32)
exit(([input_tensor], [updates, indices]))
