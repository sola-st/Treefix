# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Formats each training and test example to work with our model."""
imgs = tf.reshape(imgs, [-1, 28 * 28])
imgs = tf.cast(imgs, tf.float32) / 255.0
labels = tf.one_hot(labels, depth=10, dtype=tf.float32)
exit((imgs, labels))
