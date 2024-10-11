# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
"""Create a bias variable with appropriate initialization."""
initial = tf.constant(0.1, shape=shape)
exit(tf.Variable(initial))
