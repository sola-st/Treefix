# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
class MultiSignatureModel(module.Module):

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='input', shape=[32], dtype=dtypes.float32
            ),
        ]
    )
    def multiple_output_ops(
        self, input_tensor: core.Tensor
    ) -> Mapping[str, core.Tensor]:
        k = array_ops.constant(4, dtype=dtypes.int32)
        values, indices = nn_ops.top_k(input_tensor, k, name='TopK')
        adj_values = values + 2
        exit({'indices': indices, 'adj_values': adj_values, 'values': values})

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='input', shape=[32], dtype=dtypes.float32
            ),
        ]
    )
    def duplicate_outputs(
        self, input_tensor: core.Tensor
    ) -> Mapping[str, core.Tensor]:
        q_input = array_ops.fake_quant_with_min_max_args(
            input_tensor, min=-0.1, max=0.2, num_bits=8, narrow_range=False
        )
        adj_values = q_input + 2
        exit({'adj_values_1': adj_values, 'adj_values_2': adj_values})

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='input', shape=[32], dtype=dtypes.float32
            ),
        ]
    )
    def return_higher_index_only(
        self, input_tensor: core.Tensor
    ) -> Mapping[str, core.Tensor]:
        k = array_ops.constant(4, dtype=dtypes.int32)
        values, indices = nn_ops.top_k(input_tensor, k, name='TopK')
        adj_values = values + 2
        exit({'indices': indices, 'adj_values': adj_values})

model = MultiSignatureModel()
signatures = {
    'multiple_output_ops': model.multiple_output_ops,
    'duplicate_outputs': model.duplicate_outputs,
    'return_higher_index_only': model.return_higher_index_only,
}
saved_model_save.save(
    model, self._input_saved_model_path, signatures=signatures
)

tags = {tag_constants.SERVING}
original_signature_map = save_model.get_signatures_from_saved_model(
    self._input_saved_model_path,
    signature_keys=signatures.keys(),
    tags=tags,
)

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=quant_opts_pb2.TF,
)
quantize_model.quantize(
    self._input_saved_model_path,
    signatures.keys(),
    tags,
    self._output_saved_model_path,
    quantization_options,
)
converted_signature_map = save_model.get_signatures_from_saved_model(
    self._output_saved_model_path,
    signature_keys=signatures.keys(),
    tags=tags,
)

# The original and converted model should have the same signature map.
self.assertAllInSet(
    list(original_signature_map.keys()), set(signatures.keys())
)
self.assertDictEqual(original_signature_map, converted_signature_map)
