# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Tests the object detection model that cannot be loaded in TensorFlow.
self._initObjectDetectionArgs()

converter = lite.TFLiteConverter.from_frozen_graph(self._graph_def_file,
                                                   self._input_arrays,
                                                   self._output_arrays,
                                                   self._input_shapes)
converter.allow_custom_ops = True
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('normalized_input_image_tensor', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 300, 300, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 4)
self.assertEqual('TFLite_Detection_PostProcess', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 10, 4], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])

self.assertEqual('TFLite_Detection_PostProcess:1',
                 output_details[1]['name'])
self.assertAllEqual([1, 10], output_details[1]['shape'])
self.assertEqual('TFLite_Detection_PostProcess:2',
                 output_details[2]['name'])
self.assertAllEqual([1, 10], output_details[2]['shape'])
self.assertEqual('TFLite_Detection_PostProcess:3',
                 output_details[3]['name'])
self.assertAllEqual([1], output_details[3]['shape'])
