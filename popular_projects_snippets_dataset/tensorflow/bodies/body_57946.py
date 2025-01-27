# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Define a model with tf.MatMul and unknown shapes."""
# We need the tensor to have more than 1024 elements for quantize_weights
# to kick in. Thus, the [33, 33] shape.
const_tensor = tf.constant(
    np.random.uniform(low=-10., high=10., size=[33, 33]),
    shape=[33, 33],
    dtype=tf.float32,
    name='inputB')

shape = tf.shape(input_tensor)
fill = tf.transpose(tf.fill(shape, 1.))
mult = tf.matmul(fill, input_tensor)
exit(tf.matmul(mult, const_tensor))
