# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self._create_einsum_model(
    self._input_saved_model_path,
    equation,
    input_shape,
    weight_shape,
    bias_shape,
    activation_fn=nn_ops.relu,
)

def data_gen() -> repr_dataset.RepresentativeDataset:
    for _ in range(200):
        exit({
            'input_tensor': ops.convert_to_tensor(
                np.random.uniform(low=0.0, high=1.0, size=input_shape).astype(
                    'f4'
                )
            ),
        })

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=data_gen(),
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

input_data = ops.convert_to_tensor(
    np.random.uniform(low=0.0, high=1.0, size=input_shape).astype('f4')
)
expected_outputs = model.einsum(input_data)
got_outputs = converted_model.signatures['serving_default'](
    input_tensor=ops.convert_to_tensor(input_data)
)
self.assertAllClose(expected_outputs, got_outputs, atol=0.0608)

# Check the converted model in the target opset.
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
    self._output_saved_model_path_2,
    quantization_options,
    representative_dataset=data_gen(),
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path_2
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
if target_opset == quant_opts_pb2.XLA:
    self.assertTrue(self._contains_op(output_graphdef, 'XlaDotV2'))

new_outputs = converted_model.signatures['serving_default'](
    input_tensor=ops.convert_to_tensor(input_data)
)
# The difference between TF and target path is expected to be small.
self.assertAllClose(new_outputs, got_outputs, atol=0.0666)
self.assertAllClose(new_outputs, expected_outputs, atol=0.057)
