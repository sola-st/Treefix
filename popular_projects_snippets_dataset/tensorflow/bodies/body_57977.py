# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
saved_model_dir = os.path.join(self.get_temp_dir(),
                               'simple_mutable_variable')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[1], dtype=tf.float32, name='input')

        ta = tf.TensorArray(
            tf.float32, size=3, dynamic_size=False, clear_after_read=False)
        ta = ta.write(0, 10.0)
        ta = ta.write(1, 20.0)
        ta = ta.write(2, 30.0)

        out_tensor = ta.read(0) + ta.read(2)

        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
