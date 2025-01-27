# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a simple SavedModel."""
saved_model_dir = self._createSavedModelTwoInputArrays(shape=[1, 16, 16, 3])

_, in_tensors, out_tensors = self._convertSavedModel(
    saved_model_dir=saved_model_dir, input_arrays=["inputB", "inputA"])

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["inputA:0", "inputB:0"])
self.assertEqual(
    self._getArrayShapes(in_tensors), [[1, 16, 16, 3], [1, 16, 16, 3]])
