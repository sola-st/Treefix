# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root, func, calibration_gen = self._getIntegerQuantizeModel()
converter = lite.TFLiteConverterV2.from_concrete_functions([func], root)
converter.optimizations = [lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.target_spec.supported_types = [dtypes.float16]
quantized_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_model)
self.assertIsNotNone(metadata)
self.assertAllEqual([metadata_fb.ModelOptimizationMode.PTQ_FLOAT16],
                    metadata.options.modelOptimizationModes)
