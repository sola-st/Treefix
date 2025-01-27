# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
func, _ = self._getSqrtModel()
converter = lite.TFLiteConverterV2.from_concrete_functions(
    [func.get_concrete_function()])
converter.optimizations = [lite.Optimize.DEFAULT]
quantized_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([metadata_fb.ModelOptimizationMode.PTQ_DYNAMIC_RANGE],
                    metadata.options.modelOptimizationModes)
