# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
matrix_b_values = [
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1
]
sess, inputs, outputs = self._getSparsificableModel(matrix_b_values)
float_converter = lite.TFLiteConverter.from_session(sess, inputs, outputs)
float_converter.optimizations = [lite.Optimize.EXPERIMENTAL_SPARSITY]
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(float_tflite_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([metadata_fb.ModelOptimizationMode.RANDOM_SPARSITY],
                    metadata.options.modelOptimizationModes)
