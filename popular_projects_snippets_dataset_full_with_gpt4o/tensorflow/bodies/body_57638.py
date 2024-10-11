# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputA')
    in_tensor_2 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputB')
    out_tensor = array_ops.fake_quant_with_min_max_args(
        in_tensor_1 + in_tensor_2, min=0., max=1., name='output')
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess,
                                              [in_tensor_1, in_tensor_2],
                                              [out_tensor])
converter.inference_type = dtypes.uint8
converter.quantized_input_stats = {
    'inputA': (0., 1.),
    'inputB': (0., 1.)
}  # mean, std_dev
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEqual('inputA', input_details[0]['name'])
self.assertEqual(np.uint8, input_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((1., 0.), input_details[0]['quantization'])

self.assertEqual('inputB', input_details[1]['name'])
self.assertEqual(np.uint8, input_details[1]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[1]['shape'])
self.assertEqual((1., 0.), input_details[1]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.uint8, output_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], output_details[0]['shape'])
self.assertGreater(output_details[0]['quantization'][0], 0)  # scale
