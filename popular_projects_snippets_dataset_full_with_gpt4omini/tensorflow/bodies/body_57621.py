# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, None, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Test None after 1st dimension.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('Placeholder', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 1, 16, 3], input_details[0]['shape'])
self.assertAllEqual([1, -1, 16, 3], input_details[0]['shape_signature'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

# Resize tensor with strict checking.
with self.assertRaises(RuntimeError) as error:
    interpreter.resize_tensor_input(0, [3, 16, 16, 3], strict=True)
self.assertIn(
    'ResizeInputTensorStrict only allows mutating unknown dimensions '
    'identified by -1.', str(error.exception))

# Resize tensor and invoke.
interpreter.resize_tensor_input(0, [1, 16, 16, 3], strict=True)
interpreter.allocate_tensors()

test_input = np.full([1, 16, 16, 3], 1.0, dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], test_input)
interpreter.invoke()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertAllEqual([1, -1, 16, 3], input_details[0]['shape_signature'])

output_details = interpreter.get_output_details()
self.assertAllEqual([1, -1, 16, 3], output_details[0]['shape_signature'])
