# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
with session.Session(graph=ops.Graph()) as sess:
    input_tensor = array_ops.placeholder(
        dtypes.float32, shape=[], name='input'
    )
    q_input = array_ops.fake_quant_with_min_max_args(
        input_tensor, min=-0.1, max=0.2, num_bits=8, narrow_range=False
    )
    sqrt = math_ops.sqrt(q_input, name='sqrt')
    identity = array_ops.identity(sqrt, name='output')

    input_map = {'input': input_tensor}
    output_map = {'sqrt': identity}
    signature = signature_def_utils_impl.predict_signature_def(
        inputs=input_map, outputs=output_map
    )
    signature_map = {'main': signature}

    tags = {tag_constants.SERVING}
    v1_builder = builder.SavedModelBuilder(self._input_saved_model_path)
    v1_builder.add_meta_graph_and_variables(
        sess, tags, signature_def_map=signature_map
    )
    v1_builder.save()

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=quant_opts_pb2.TF,
)
quantize_model.quantize(
    self._input_saved_model_path,
    signature_map.keys(),
    tags,
    self._output_saved_model_path,
    quantization_options,
)
converted_signature_map = save_model.get_signatures_from_saved_model(
    self._output_saved_model_path,
    signature_keys=signature_map.keys(),
    tags=tags,
)
# The original and converted model should have the same signature map.
self.assertDictEqual(signature_map, converted_signature_map)
