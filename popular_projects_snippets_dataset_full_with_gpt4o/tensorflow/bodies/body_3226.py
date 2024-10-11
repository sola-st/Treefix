# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
input_shape = (1, 512)

self._create_matmul_model(
    input_shape=input_shape,
    weight_shape=(512, 2),
    saved_model_path=self._input_saved_model_path,
)

tags = {tag_constants.SERVING}
quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.WEIGHT_ONLY
    ),
    op_set=target_opset,
    enable_per_channel_quantization=enable_per_channel_quantization,
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

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def

self.assertTrue(self._contains_op(output_graphdef, 'MatMul'))
# Due to other meta data, the compression is not exactly 1/4.
threshold = 0.9 if quant_opts_pb2.TF else 0.3
self.assertSizeRatioLessThan(
    self._output_saved_model_path, self._input_saved_model_path, threshold
)
