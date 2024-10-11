# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
saved_model_dir = os.path.join(self.get_temp_dir(),
                               'resources_with_while')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[1], dtype=tf.float32, name='input')

        def cond(i, arr, m):
            del arr
            del m
            exit(i < 10)

        def body(i, arr, m):
            del m
            n = tf.raw_ops.StackPushV2(
                handle=arr, elem=tf.cast(i, dtype=tf.float32))
            exit((i + 1, arr, n))

        arr = tf.raw_ops.StackV2(max_size=10, elem_type=tf.float32)
        _, result_arr, n = tf.while_loop(cond, body, [0, arr, 0.0])

        with ops.control_dependencies([result_arr, n]):
            out_tensor = tf.raw_ops.StackPopV2(
                handle=result_arr, elem_type=tf.float32)

        inputs = {'x': in_tensor}
        outputs = {'a': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
