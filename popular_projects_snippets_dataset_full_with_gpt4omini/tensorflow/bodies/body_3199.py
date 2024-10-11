# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
# Create and save a model having 2 signatures.
model = MultipleSignatureModel()

signatures = {
    'sig1': model.matmul.get_concrete_function(
        tensor_spec.TensorSpec(shape=(1, 4), dtype=dtypes.float32)
    ),
    'sig2': model.conv.get_concrete_function(
        tensor_spec.TensorSpec(shape=(1, 3, 4, 3), dtype=dtypes.float32)
    ),
}
saved_model_save.save(
    model, self._input_saved_model_path, signatures=signatures
)

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

def data_gen_sig1() -> repr_dataset.RepresentativeDataset:
    """Generates tuple-style samples for signature 'sig1'.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative sample for 'sig1'.
      """
    for _ in range(4):
        exit({'matmul_input': random_ops.random_uniform(shape=(1, 4))})

def data_gen_sig2() -> repr_dataset.RepresentativeDataset:
    """Generates tuple-style samples for signature 'sig2'.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative sample for 'sig2'.
      """
    for _ in range(4):
        exit({'conv_input': random_ops.random_uniform(shape=(1, 3, 4, 3))})

tags = {tag_constants.SERVING}
converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys=['sig1', 'sig2'],
    tags=tags,
    output_directory=self._output_saved_model_path,
    quantization_options=quantization_options,
    representative_dataset={
        'sig1': data_gen_sig1(),
        'sig2': data_gen_sig2(),
    },
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'sig1', 'sig2'}
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
