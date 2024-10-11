# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
matrix_b_values = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0
]
sess, inputs, outputs = self._getSparsificableModel(matrix_b_values)
converter = lite.TFLiteConverter.from_session(sess, inputs, outputs)
converter.optimizations = {lite.Optimize.EXPERIMENTAL_SPARSITY}
tflite_model = converter.convert()
self.assertTrue(tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([
    metadata_fb.ModelOptimizationMode.BLOCK_SPARSITY,
], metadata.options.modelOptimizationModes)
