# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()
# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_index = interpreter.get_input_details()[0]['index']
dummy_tensor = np.ones(shape=[1, 16, 16, 3], dtype=np.float32)
with self.assertRaises(ValueError):
    interpreter.set_tensor(input_index, dummy_tensor)
