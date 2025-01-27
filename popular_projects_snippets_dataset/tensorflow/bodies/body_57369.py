# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel that fails due to an invalid signature_key."""
saved_model_dir = self._createSimpleSavedModel(shape=[1, 16, 16, 3])
with self.assertRaises(ValueError) as error:
    self._convertSavedModel(saved_model_dir, signature_key="invalid-key")
self.assertEqual(
    "No 'invalid-key' in the SavedModel's SignatureDefs. "
    "Possible values are 'serving_default'.", str(error.exception))
