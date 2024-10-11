# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
matrix_b_values = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0
]
root, func = self._getSparsificableModel(matrix_b_values)
float_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                 root)
float_converter.optimizations = [lite.Optimize.EXPERIMENTAL_SPARSITY]
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)
# Check the conversion metadata.
metadata = get_conversion_metadata(float_tflite_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([metadata_fb.ModelOptimizationMode.BLOCK_SPARSITY],
                    metadata.options.modelOptimizationModes)
