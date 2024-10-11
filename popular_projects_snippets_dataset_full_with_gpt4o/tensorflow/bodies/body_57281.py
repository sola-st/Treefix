# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/metrics/blazeface_metrics.py
tf.reset_default_graph()
with tf.Graph().as_default():
    expected_box_encodings = tf.placeholder(
        dtype=tf.float32, shape=[1, 564, 16])
    expected_scores = tf.placeholder(dtype=tf.float32, shape=[1, 564, 1])
    actual_box_encodings = tf.placeholder(dtype=tf.float32, shape=[1, 564, 16])
    actual_scores = tf.placeholder(dtype=tf.float32, shape=[1, 564, 1])

    [kld_metric, box_mse, ok] = metrics(expected_box_encodings, expected_scores,
                                        actual_box_encodings, actual_scores)
    ok = tf.reshape(ok, [1], name='ok')
    kld_metric = tf.reshape(kld_metric, [1], name='symmetric_kl_divergence')
    box_mse = tf.reshape(box_mse, [1], name='box_mse')
    sess = tf.compat.v1.Session()
    converter = tf.lite.TFLiteConverter.from_session(sess, [
        expected_box_encodings, expected_scores, actual_box_encodings,
        actual_scores
    ], [kld_metric, box_mse, ok])
    converter.experimental_new_converter = True
    tflite_model = converter.convert()
    open(output_path, 'wb').write(tflite_model)
