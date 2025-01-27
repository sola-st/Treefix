# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Create a simple SavedModel with a certain shape."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'input_shape_model')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        unknown_shape = tf.TensorShape(shape)
        in_tensor = tf.compat.v1.placeholder(
            shape=unknown_shape, dtype=tf.float32, name='input')
        out_tensor = in_tensor + in_tensor
        inputs = {'input': in_tensor}
        outputs = {'output': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
