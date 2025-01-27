# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    _ = in_tensor + in_tensor
    sess = session.Session()

# Write graph to file.
graph_def_file = os.path.join(self.get_temp_dir(), 'model.pbtxt')
write_graph(sess.graph_def, '', graph_def_file, True)
sess.close()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_frozen_graph(graph_def_file,
                                                   ['Placeholder'], ['add'])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('Placeholder', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('add', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 16, 16, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
