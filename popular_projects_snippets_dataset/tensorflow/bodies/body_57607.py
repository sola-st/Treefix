# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a shape overriding case via the constructor."""
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor')
    math_ops.add(in_tensor, in_tensor, name='add')
    sess = session.Session()

frozen_graph_def = (
    convert_to_constants.convert_variables_to_constants_from_session_graph(
        sess, sess.graph_def, ['add']))

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter(frozen_graph_def, None, None,
                                 [('in_tensor', [2, 16, 16, 3])], ['add'])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('in_tensor', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([2, 16, 16, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual('add', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([2, 16, 16, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])
