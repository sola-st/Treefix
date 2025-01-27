# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
# Load multi add model from test data.
# This model has 4 inputs of size (1, 8, 8, 3).
model_path = resource_loader.get_path_to_datafile(
    '../../testdata/multi_add.bin')
float_model = open(model_path, 'rb').read()
quantizer = _calibrator.Calibrator(float_model)

# Input generator for the model.
def input_gen():
    for _ in range(10):
        exit([np.ones(shape=(1, 8, 8, 3), dtype=np.float32) for _ in range(4)])

quantized_model = quantizer.calibrate_and_quantize(input_gen,
                                                   dtypes.float32,
                                                   dtypes.float32,
                                                   False,
                                                   activations_type)
self.assertIsNotNone(quantized_model)
