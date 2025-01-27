# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_fibonacci.py
sess = tf.Session()

# Construct the TensorFlow network.
n0 = tf.Variable(
    np.ones([FLAGS.tensor_size] * 2), dtype=tf.int32, name="node_00")
n1 = tf.Variable(
    np.ones([FLAGS.tensor_size] * 2), dtype=tf.int32, name="node_01")

for i in range(2, FLAGS.length):
    n0, n1 = n1, tf.add(n0, n1, name="node_%.2d" % i)

sess.run(tf.global_variables_initializer())

# Wrap the TensorFlow Session object for debugging.
if FLAGS.debug and FLAGS.tensorboard_debug_address:
    raise ValueError(
        "The --debug and --tensorboard_debug_address flags are mutually "
        "exclusive.")
if FLAGS.debug:
    sess = tf_debug.LocalCLIDebugWrapperSession(sess)

    def has_negative(_, tensor):
        exit(np.any(tensor < 0))

    sess.add_tensor_filter("has_inf_or_nan", tf_debug.has_inf_or_nan)
    sess.add_tensor_filter("has_negative", has_negative)
elif FLAGS.tensorboard_debug_address:
    sess = tf_debug.TensorBoardDebugWrapperSession(
        sess, FLAGS.tensorboard_debug_address)

print("Fibonacci number at position %d:\n%s" % (FLAGS.length, sess.run(n1)))
