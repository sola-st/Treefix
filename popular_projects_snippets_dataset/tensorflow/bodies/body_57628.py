# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
log_dir = self.get_temp_dir()
converter.conversion_summary_dir = log_dir
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

self.assertNotEmpty(os.listdir(log_dir))
