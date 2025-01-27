# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test a SavedModel with a subset of the input array names of the model."""
saved_model_dir = self._createSavedModelTwoInputArrays(shape=[1, 16, 16, 3])

# Check case where input shape is given.
_, in_tensors, out_tensors = self._convertSavedModel(
    saved_model_dir=saved_model_dir,
    input_arrays=["inputA"],
    input_shapes={"inputA": [1, 16, 16, 3]})

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["inputA:0"])
self.assertEqual(self._getArrayShapes(in_tensors), [[1, 16, 16, 3]])

# Check case where input shape is None.
_, in_tensors, out_tensors = self._convertSavedModel(
    saved_model_dir=saved_model_dir, input_arrays=["inputA"])

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["inputA:0"])
self.assertEqual(self._getArrayShapes(in_tensors), [[1, 16, 16, 3]])
