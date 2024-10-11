# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Ensures that resize_tensor_input(strict=True) works as expected.
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

# Resize incorrect value.
with self.assertRaises(RuntimeError) as error:
    interpreter.resize_tensor_input(0, [3, 16, 16, 3], strict=True)
self.assertIn(
    'ResizeInputTensorStrict only allows mutating unknown dimensions '
    'identified by -1.', str(error.exception))

# Resize correct value.
interpreter.resize_tensor_input(0, [1, 16, 16, 3], strict=True)
interpreter.allocate_tensors()
