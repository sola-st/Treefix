# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
tags = {tag_constants.SERVING}

input_placeholder = self._create_and_save_tf1_gather_model(
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
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

data_gen = self._create_data_generator(
    input_key='x',
    shape=input_placeholder.shape,
    minval=0,
    maxval=10,
    dtype=dtypes.int64,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=data_gen,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), signature_keys
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
# Quantization is not currently supported for gather.
self.assertFalse(self._contains_quantized_function_call(output_graphdef))
