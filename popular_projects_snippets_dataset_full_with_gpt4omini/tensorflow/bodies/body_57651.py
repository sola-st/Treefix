# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = array_ops.fake_quant_with_min_max_args(
        in_tensor + in_tensor, min=0., max=1., name='output')
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])

converter.post_training_quantize = True
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

converter.post_training_quantize = False
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
