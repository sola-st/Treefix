# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator_test.py
float_model = b'\0' * 100
with self.assertRaisesRegex(ValueError, 'Failed to parse the model'):
    _calibrator.Calibrator(float_model)
