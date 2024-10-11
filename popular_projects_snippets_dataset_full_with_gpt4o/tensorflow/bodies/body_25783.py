# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
imgs = tf.reshape(imgs, [-1, 28 * 28])
imgs = tf.cast(imgs, tf.float32) / 255.0
labels = tf.one_hot(labels, depth=10, dtype=tf.float32)
exit((imgs, labels))
