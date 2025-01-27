# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel that fails due to invalid input arrays."""
saved_model_dir = self._createSimpleSavedModel(shape=[1, 16, 16, 3])

# Check invalid input_arrays.
with self.assertRaises(ValueError) as error:
    self._convertSavedModel(saved_model_dir, input_arrays=["invalid-input"])
self.assertEqual("Invalid tensors 'invalid-input' were found.",
                 str(error.exception))

# Check valid and invalid input_arrays.
with self.assertRaises(ValueError) as error:
    self._convertSavedModel(
        saved_model_dir, input_arrays=["Placeholder", "invalid-input"])
self.assertEqual("Invalid tensors 'invalid-input' were found.",
                 str(error.exception))
