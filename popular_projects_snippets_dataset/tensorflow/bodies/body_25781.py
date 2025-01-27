# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_errors.py
sess = tf.Session()

# Construct the TensorFlow network.
ph_float = tf.placeholder(tf.float32, name="ph_float")
x = tf.transpose(ph_float, name="x")
v = tf.Variable(np.array([[-2.0], [-3.0], [6.0]], dtype=np.float32), name="v")
m = tf.constant(
    np.array([[0.0, 1.0, 2.0], [-4.0, -1.0, 0.0]]),
    dtype=tf.float32,
    name="m")
y = tf.matmul(m, x, name="y")
z = tf.matmul(m, v, name="z")

if FLAGS.debug:
    if FLAGS.use_random_config_path:
        _, config_file_path = tempfile.mkstemp(".tfdbg_config")
    else:
        config_file_path = None
    sess = tf_debug.LocalCLIDebugWrapperSession(
        sess, ui_type=FLAGS.ui_type, config_file_path=config_file_path)

if FLAGS.error == "shape_mismatch":
    print(sess.run(y, feed_dict={ph_float: np.array([[0.0], [1.0], [2.0]])}))
elif FLAGS.error == "uninitialized_variable":
    print(sess.run(z))
elif FLAGS.error == "no_error":
    print(sess.run(y, feed_dict={ph_float: np.array([[0.0, 1.0, 2.0]])}))
else:
    raise ValueError("Unrecognized error type: " + FLAGS.error)
