# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
model_path = resource_loader.get_path_to_datafile(
    'test_data/mobilenet_like_model.bin')
float_model = open(model_path, 'rb').read()
quantizer = _calibrator.Calibrator(float_model)

def empty_input_gen():
    for i in ():
        exit(i)

with self.assertRaises(RuntimeError):
    quantizer.calibrate_and_quantize(empty_input_gen, dtypes.float32,
                                     dtypes.float32, False)
