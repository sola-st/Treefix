# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Create a simple SavedModel."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'simple_savedmodel')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor_1 = tf.compat.v1.placeholder(
            shape=shape, dtype=tf.float32, name='inputB')
        in_tensor_2 = tf.compat.v1.placeholder(
            shape=shape, dtype=tf.float32, name='inputA')
        variable_node = tf.Variable(1.0, name='variable_node')
        out_tensor = in_tensor_1 + in_tensor_2 * variable_node
        inputs = {'x': in_tensor_1, 'y': in_tensor_2}
        outputs = {'z': out_tensor}
        sess.run(tf.compat.v1.variables_initializer([variable_node]))
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
