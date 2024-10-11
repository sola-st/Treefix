# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a SavedModel with a matrix input."""
saved_model_dir = self._createModelWithInputShape([2, 3])

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
self.assertTrue(tflite_model)

# Validate that matrix tensors have a rank = 2.
tflite_model_obj = _convert_bytearray_to_object(tflite_model)
for tensor in tflite_model_obj.subgraphs[0].tensors:
    self.assertEqual(True, tensor.hasRank)
    self.assertEqual([2, 3], tensor.shape.tolist())
