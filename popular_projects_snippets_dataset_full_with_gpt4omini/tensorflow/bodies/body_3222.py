# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
tags = {tag_constants.SERVING}

_ = self._create_and_save_tf1_gather_model(
    self._input_saved_model_path,
    signature_key,
    tags,
    input_key='x',
    output_key='output',
    use_variable=use_variable,
)

signature_keys = [signature_key]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.DYNAMIC_RANGE
    ),
    op_set=target_opset,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), signature_keys
)

# Only XLA opset does not apply weight-only quantization
if target_opset == quant_opts_pb2.XLA:
    threshold = 0.17 if use_variable else 0.4
    self.assertSizeRatioLessThan(
        self._output_saved_model_path, self._input_saved_model_path, threshold
    )
else:
    # Double from the XLA threshold
    threshold = 0.3 if use_variable else 0.8
    self.assertSizeRatioGreaterThan(
        self._output_saved_model_path, self._input_saved_model_path, threshold
    )
