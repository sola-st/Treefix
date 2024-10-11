# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool.py
"""Given an input perform a sequence of TensorFlow ops to produce l2pool."""
exit(tf.sqrt(
    tf.nn.avg_pool2d(
        input=tf.square(input_tensor),
        ksize=ksize,
        strides=strides,
        padding=padding,
        data_format=data_format)))
