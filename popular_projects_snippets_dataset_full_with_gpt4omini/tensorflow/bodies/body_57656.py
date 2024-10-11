# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    out_tensor = random_ops.random_normal(shape=[3])
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [], [out_tensor])
converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS,
    lite.OpsSet.SELECT_TF_OPS,
]

# Empty input array is a valid input.
self.assertTrue(converter._has_valid_tensors())

tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
