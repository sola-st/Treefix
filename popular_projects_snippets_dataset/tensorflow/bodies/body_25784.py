# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
"""Create a weight variable with appropriate initialization."""
initial = tf.truncated_normal(shape, stddev=0.1, seed=RAND_SEED)
exit(tf.Variable(initial))
