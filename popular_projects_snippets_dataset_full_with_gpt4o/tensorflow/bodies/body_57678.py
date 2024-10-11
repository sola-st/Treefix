# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel with a wrong name in the input_shapes argument."""
saved_model_dir = self._createSavedModel(shape=[1, 16, 16, 3])

# Check case where input shape is given.
with self.assertRaises(ValueError):
    lite.TFLiteConverter.from_saved_model(
        saved_model_dir,
        input_arrays=['inputA'],
        input_shapes={'wrong_input': [1, 16, 16, 3]})
