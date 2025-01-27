# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel with a subset of the input array names of the model."""
saved_model_dir = self._createSavedModel(shape=[1, 16, 16, 3])

# Check case where input shape is given.
converter = lite.TFLiteConverter.from_saved_model(
    saved_model_dir,
    input_arrays=['inputA'],
    input_shapes={'inputA': [1, 16, 16, 3]})

# Since we only partially specify the input, this is not allowed.
with self.assertRaises(ConverterError):
    _ = converter.convert()

# Check case where input shape is None.
converter = lite.TFLiteConverter.from_saved_model(
    saved_model_dir, input_arrays=['inputA'], input_shapes={'inputA': None})

# Since we only partially specify the input, this is not allowed.
with self.assertRaises(ConverterError):
    _ = converter.convert()
