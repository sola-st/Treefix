# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
tags = {tag_constants.SERVING}

# Create two models and add them to a same SavedModel under different
# signature keys.
with ops.Graph().as_default(), session.Session() as sess:
    in_placeholder_1, output_tensor_1 = self._create_simple_tf1_conv_model()
    sig_def_1 = signature_def_utils_impl.predict_signature_def(
        inputs={'x1': in_placeholder_1}, outputs={'output1': output_tensor_1}
    )

    in_placeholder_2, output_tensor_2 = self._create_simple_tf1_conv_model()
    sig_def_2 = signature_def_utils_impl.predict_signature_def(
        inputs={'x2': in_placeholder_2}, outputs={'output2': output_tensor_2}
    )

    v1_builder = builder.SavedModelBuilder(self._input_saved_model_path)
    v1_builder.add_meta_graph_and_variables(
        sess,
        tags,
        signature_def_map={
            'sig1': sig_def_1,
            'sig2': sig_def_2,
        },
    )

    v1_builder.save()

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

def data_gen_sig1() -> repr_dataset.RepresentativeDataset:
    """Generates tuple-style samples.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative samples for signature 'sig1'.
      """
    for _ in range(4):
        exit({'x1': random_ops.random_uniform(shape=in_placeholder_1.shape)})

def data_gen_sig2() -> repr_dataset.RepresentativeDataset:
    """Generates tuple-style samples.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative samples for signature 'sig2'.
      """
    for _ in range(4):
        exit({'x2': random_ops.random_uniform(shape=in_placeholder_2.shape)})

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
