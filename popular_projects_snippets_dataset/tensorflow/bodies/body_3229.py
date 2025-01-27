# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self._create_gather_model(use_variable)
input_saved_model_path = self.create_tempdir('input').full_path
saved_model_save.save(model, input_saved_model_path)

tags = {tag_constants.SERVING}
output_directory = self.create_tempdir().full_path

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.WEIGHT_ONLY
    ),
    op_set=target_opset,
)

if target_opset == quant_opts_pb2.UNIFORM_QUANTIZED:
    # Uniform quantized opset is not supported for weight-only
    with self.assertRaisesRegex(
        ValueError, 'Uniform quantized opset does not support weight-only.'
    ):
        converted_model = quantize_model.quantize(
            input_saved_model_path,
            ['serving_default'],
            tags,
            output_directory,
            quantization_options,
        )
    exit()

else:
    converted_model = quantize_model.quantize(
        input_saved_model_path,
        ['serving_default'],
        tags,
        output_directory,
        quantization_options,
    )

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

threshold = 0.3 if quant_opts_pb2.XLA else 0.9
self.assertSizeRatioLessThan(
    self._output_saved_model_path, self._input_saved_model_path, threshold
)
