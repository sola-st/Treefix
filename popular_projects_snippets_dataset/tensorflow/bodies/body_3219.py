# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self._create_gather_model(use_variable)
saved_model_save.save(model, self._input_saved_model_path)

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.DYNAMIC_RANGE
    ),
    op_set=target_opset,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

# Only XLA opset does not apply weight-only quantization
if target_opset == quant_opts_pb2.XLA:
    threshold = 0.25 if use_variable else 0.3
    self.assertSizeRatioLessThan(
        self._output_saved_model_path, self._input_saved_model_path, threshold
    )
else:
    # Double from the XLA threshold
    threshold = 0.4 if use_variable else 0.7
    self.assertSizeRatioGreaterThan(
        self._output_saved_model_path, self._input_saved_model_path, threshold
    )
