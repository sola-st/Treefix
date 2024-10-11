# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_keras.py
# Create a dummy dataset.
num_examples = 8
steps_per_epoch = 2
input_dims = 3
output_dims = 1
xs = np.zeros([num_examples, input_dims])
ys = np.zeros([num_examples, output_dims])
dataset = tf.data.Dataset.from_tensor_slices(
    (xs, ys)).repeat(num_examples).batch(int(num_examples / steps_per_epoch))

sess = tf.Session()
if FLAGS.debug:
    # Use the command-line interface (CLI) of tfdbg.
    if FLAGS.use_random_config_path:
        _, config_file_path = tempfile.mkstemp(".tfdbg_config")
    else:
        config_file_path = None
    sess = tf_debug.LocalCLIDebugWrapperSession(
        sess, ui_type=FLAGS.ui_type, config_file_path=config_file_path)
elif FLAGS.tensorboard_debug_address:
    # Use the TensorBoard Debugger Plugin (GUI of tfdbg).
    sess = tf_debug.TensorBoardDebugWrapperSession(
        sess, FLAGS.tensorboard_debug_address)
tf.keras.backend.set_session(sess)

# Create a dummy model.
model = tf.keras.Sequential(
    [tf.keras.layers.Dense(1, input_shape=[input_dims])])
model.compile(loss="mse", optimizer="sgd")

# Train the model using the dummy dataset created above.
model.fit(dataset, epochs=FLAGS.epochs, steps_per_epoch=steps_per_epoch)
