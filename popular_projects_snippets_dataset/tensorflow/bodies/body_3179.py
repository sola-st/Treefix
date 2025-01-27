# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self._create_simple_gather_and_conv_model(filter_shape=(2, 3, 3, 2))
saved_model_save.save(model, self._input_saved_model_path)

data_gen = self._create_data_generator(
    input_key='input_tensor',
    shape=[6],
    minval=0,
    maxval=10,
    dtype=dtypes.int64,
)

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=target_opset,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=data_gen,
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
if target_opset == quant_opts_pb2.XLA:
    self.assertTrue(self._contains_op(output_graphdef, 'XlaConvV2'))
    self.assertSizeRatioLessThan(
        self._output_saved_model_path, self._input_saved_model_path, 1 / 3
    )
elif target_opset == quant_opts_pb2.UNIFORM_QUANTIZED:
    # _contains_op for UQ ops also checks _contains_quantized_function_call.
    self.assertTrue(
        self._contains_op(output_graphdef, 'UniformQuantizedConvolution')
    )
    self.assertSizeRatioGreaterThan(
        self._output_saved_model_path, self._input_saved_model_path, 0.95
    )
else:
    self.assertTrue(self._contains_quantized_function_call(output_graphdef))
    self.assertSizeRatioGreaterThan(
        self._output_saved_model_path, self._input_saved_model_path, 0.95
    )
