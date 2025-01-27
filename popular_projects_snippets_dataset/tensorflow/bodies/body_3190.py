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

# Use plain python lists as representative samples.
representative_dataset = [
    {
        'input_tensor': [[i * 0.1 for i in range(1024)]],
    }
    for _ in range(4)
]

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options=quantization_options,
    representative_dataset=representative_dataset,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
