# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self.SimpleModel()

saved_model_save.save(model, self._input_saved_model_path)

# Use default QuantizationOptions.
converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    representative_dataset=self._simple_model_data_gen(),
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

# Indirectly prove that it is performing a static-range quantization
# by checking that it complains about representative_dataset when it is
# not provided.
with self.assertRaisesRegex(ValueError, 'representative_dataset'):
    quantize_model.quantize(self._input_saved_model_path)
