# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
model_path = resource_loader.get_path_to_datafile(
    'test_data/mobilenet_like_model.bin')
model = open(model_path, 'rb').read()
added_model = _calibrator.add_intermediate_tensors(model)
self.assertIsNotNone(added_model)
