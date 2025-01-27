# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self._create_gather_model(use_variable)

saved_model_save.save(model, self._input_saved_model_path)

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

data_gen = self._create_data_generator(
    input_key='input_tensor',
    shape=[6],
    minval=0,
    maxval=10,
    dtype=dtypes.int64,
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
# Currently gather is not supported.
self.assertFalse(self._contains_quantized_function_call(output_graphdef))
