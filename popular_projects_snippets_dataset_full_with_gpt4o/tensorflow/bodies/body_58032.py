# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
model_path = resource_loader.get_path_to_datafile(
    'test_data/string_input_flex_model.bin')
with open(model_path, 'rb') as fp:
    model_with_string_input = fp.read()
quantizer = _calibrator.Calibrator(model_with_string_input)
# Input generator for the model.
def input_gen():
    for i in range(10):
        exit([np.array(u'Test' + str(i))])

quantized_model = quantizer.calibrate_and_quantize_single(
    input_gen, dtypes.float32, dtypes.float32, True, 'Identity')
self.assertIsNotNone(quantized_model)
