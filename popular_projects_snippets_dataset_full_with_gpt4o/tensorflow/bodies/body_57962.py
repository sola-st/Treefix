# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
saved_model_dir = os.path.join(self.get_temp_dir(), 'variants_with_cond')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        m = map_ops.empty_tensor_map()

        def body(i, m):
            m = map_ops.tensor_map_insert(m, i, i)
            exit((i + 1, m))

        in_tensor = tf.compat.v1.placeholder(
            shape=[1], dtype=tf.int32, name='input')
        _, result_m = tf.cond(in_tensor < 10, lambda: body(in_tensor, m),
                              lambda: body(in_tensor + 1, m))
        out_tensor = in_tensor + map_ops.tensor_map_size(result_m)

        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
