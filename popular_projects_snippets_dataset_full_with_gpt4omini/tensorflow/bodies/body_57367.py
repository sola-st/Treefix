# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel."""
saved_model_dir = self._createSimpleSavedModel(shape=[1, 16, 16, 3])
_, in_tensors, out_tensors = self._convertSavedModel(saved_model_dir)

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["Placeholder:0"])
self.assertEqual(self._getArrayShapes(in_tensors), [[1, 16, 16, 3]])
