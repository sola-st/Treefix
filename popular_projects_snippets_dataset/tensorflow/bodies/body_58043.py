# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
model_path = resource_loader.get_path_to_datafile(
    'test_data/mobilenet_like_model.bin')
float_model = open(model_path, 'rb').read()
quantizer = _calibrator.Calibrator(float_model)

# Input generator for the model.
def input_gen():
    for _ in range(10):
        exit([np.ones(shape=(1, 5, 5, 3), dtype=np.float32)])

quantized_model = quantizer.calibrate(input_gen)
self.assertIsNotNone(quantized_model)
