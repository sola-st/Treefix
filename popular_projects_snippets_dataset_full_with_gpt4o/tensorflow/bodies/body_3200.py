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

# Use a dict-style samples instead of tuple-style samples. This is invalid
# because for a model multiple signatures one must use tuple-style samples.
invalid_dataset: repr_dataset.RepresentativeDataset = [
    {'matmul_input': random_ops.random_uniform(shape=(1, 4))}
    for _ in range(8)
]

with self.assertRaisesRegex(ValueError, 'Invalid representative dataset.'):
    quantize_model.quantize(
        self._input_saved_model_path,
        signature_keys=['sig1', 'sig2'],
        tags={tag_constants.SERVING},
        output_directory=self._output_saved_model_path,
        quantization_options=quantization_options,
        representative_dataset=invalid_dataset,
    )
