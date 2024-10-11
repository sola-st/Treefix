# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel that fails due to invalid output arrays."""
saved_model_dir = self._createSimpleSavedModel(shape=[1, 16, 16, 3])
with self.assertRaises(ValueError) as error:
    self._convertSavedModel(saved_model_dir, output_arrays=["invalid-output"])
self.assertEqual("Invalid tensors 'invalid-output' were found.",
                 str(error.exception))
