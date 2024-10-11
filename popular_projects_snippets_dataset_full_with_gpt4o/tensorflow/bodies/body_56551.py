# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize_test.py
model = test_utils.build_mock_flatbuffer_model()
model_dict = visualize.CreateDictFromFlatbuffer(model)
self.assertEqual(test_utils.TFLITE_SCHEMA_VERSION, model_dict['version'])
self.assertEqual(1, len(model_dict['subgraphs']))
self.assertEqual(1, len(model_dict['operator_codes']))
self.assertEqual(3, len(model_dict['buffers']))
self.assertEqual(3, len(model_dict['subgraphs'][0]['tensors']))
self.assertEqual(0, model_dict['subgraphs'][0]['tensors'][0]['buffer'])
