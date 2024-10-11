# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel with correct input_arrays and input_shapes."""
saved_model_dir = self._createSimpleSavedModel(shape=[1, 16, 16, 3])
_, in_tensors, out_tensors = self._convertSavedModel(
    saved_model_dir=saved_model_dir,
    input_arrays=["Placeholder"],
    input_shapes={"Placeholder": [1, 16, 16, 3]})

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["Placeholder:0"])
self.assertEqual(self._getArrayShapes(in_tensors), [[1, 16, 16, 3]])
