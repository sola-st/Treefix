# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
saved_model_dir = os.path.join(self.get_temp_dir(), 'simple_resources')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[1], dtype=tf.float32, name='input')

        stack = tf.raw_ops.StackV2(max_size=10, elem_type=tf.float32)
        w = tf.raw_ops.StackPushV2(handle=stack, elem=in_tensor)
        with ops.control_dependencies([w]):
            a = in_tensor + in_tensor
            with ops.control_dependencies([a]):
                out_tensor = a + tf.raw_ops.StackPopV2(
                    handle=stack, elem_type=tf.float32)

        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
