# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_fibonacci_v2.py
# Wrap the TensorFlow Session object for debugging.
# TODO(anthonyjliu): Enable debugger from flags
if FLAGS.debug and FLAGS.tensorboard_debug_address:
    raise ValueError(
        "The --debug and --tensorboard_debug_address flags are mutually "
        "exclusive.")
if FLAGS.debug:
    raise NotImplementedError(
        "tfdbg v2 support for debug_fibonacci is not implemented yet")
elif FLAGS.tensorboard_debug_address:
    raise NotImplementedError(
        "Tensorboard Debugger Plugin support for debug_fibonacci_v2 is not "
        "implemented yet"
    )

# Construct the TensorFlow network.
n0 = tf.constant(np.ones([FLAGS.tensor_size] * 2), dtype=tf.int32)
n1 = tf.constant(np.ones([FLAGS.tensor_size] * 2), dtype=tf.int32)

for _ in range(2, FLAGS.length):
    n0, n1 = n1, tf.add(n0, n1)

print("Fibonacci number at position %d:\n%s" % (FLAGS.length, n1.numpy()))
