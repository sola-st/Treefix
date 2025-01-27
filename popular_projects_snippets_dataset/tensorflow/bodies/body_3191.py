# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
self._create_matmul_model(
    input_shape=(1, 1024),
    weight_shape=(1024, 3),
    saved_model_path=self._input_saved_model_path,
)

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)
tags = {tag_constants.SERVING}
signature_def_keys = [signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

representative_dataset: repr_dataset.RepresentativeDataset = [
    {
        'input_tensor': random_ops.random_uniform(shape=(1, 1024)),
    }
    for _ in range(8)
]

# Test the first run.
converted_model_1 = quantize_model.quantize(
    self._input_saved_model_path,
    signature_def_keys,
    output_directory=self._output_saved_model_path,
    quantization_options=quantization_options,
    representative_dataset=representative_dataset,
)

self.assertIsNotNone(converted_model_1)
self.assertCountEqual(
    converted_model_1.signatures._signatures.keys(), signature_def_keys
)
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))

# Test the second run on the same model.
converted_model_2 = quantize_model.quantize(
    self._input_saved_model_path,
    signature_def_keys,
    output_directory=self._output_saved_model_path_2,
    quantization_options=quantization_options,
    representative_dataset=representative_dataset,
)

self.assertIsNotNone(converted_model_2)
self.assertCountEqual(
    converted_model_2.signatures._signatures.keys(), signature_def_keys
)
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path_2
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
