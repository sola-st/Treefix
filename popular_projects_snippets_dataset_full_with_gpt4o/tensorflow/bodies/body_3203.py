# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
tags = {tag_constants.SERVING}

input_placeholder = self._create_and_save_tf1_conv_model(
    self._input_saved_model_path,
    signature_key,
    tags,
    input_key='x',
    output_key='output',
    input_shape=(1, 16, 16, 8),
    # Uses large filter to exceed the constant size threshold of 64KiB
    # (specified by `kDefaultConstantSizeThresholdInBytes`) for unfreezing.
    filter_shape=(256, 8, 8, 16),
    use_variable=True,
)

signature_keys = [signature_key]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    freeze_all_variables=quant_opts_pb2.FreezeAllVariables(enabled=False),
)

repr_ds = self._create_data_generator(
    input_key='x', shape=input_placeholder.shape, num_examples=2
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=repr_ds,
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

# Checks that quantization is applied.
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))

# Tests that there are variables in the model.
variable_node_defs = _find_variables(output_graphdef)
self.assertLen(variable_node_defs, 1)

# Reads the variables from the checkpoint file and matches with the
# variables found in the graph.
checkpoint_path = os.path.join(
    self._output_saved_model_path, 'variables', 'variables'
)
var_name_and_shapes = checkpoint_utils.list_variables(checkpoint_path)

# Checks that each variable's name and shape match.
self.assertEqual(len(variable_node_defs), len(var_name_and_shapes))
for var_name, shape in var_name_and_shapes:
    self.assertIn(var_name, variable_node_defs)
    self.assertEqual(
        shape,
        tensor_shape.TensorShape(
            variable_node_defs[var_name].attr['shape'].shape
        ),
    )
