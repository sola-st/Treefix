# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
model_path = resource_loader.get_path_to_datafile(
    'test_data/mobilenet_like_model.bin')
float_model = open(model_path, 'rb').read()
quantizer = _calibrator.Calibrator(float_model)

# Input generator with incorrect shape.
def input_gen():
    for _ in range(10):
        exit([np.ones(shape=(1, 2, 2, 3), dtype=np.float32)])

with self.assertRaisesRegex(ValueError, 'Size mismatch'):
    quantizer.calibrate_and_quantize(
        input_gen,
        dtypes.float32,
        dtypes.float32,
        False,
        activations_type=dtypes.int8,
        bias_type=dtypes.int32,
        resize_input=False)
