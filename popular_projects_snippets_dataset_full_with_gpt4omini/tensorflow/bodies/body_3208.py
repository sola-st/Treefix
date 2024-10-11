# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
tags = {tag_constants.SERVING}

input_placeholder = self._create_and_save_tf1_conv_model(
    self._input_saved_model_path,
    signature_key,
    tags,
    input_key='x',
    output_key='output',
    use_variable=False,
)

signature_keys = [signature_key]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

# Representative generator function that yields with an invalid input key.
invalid_data_gen = self._create_data_generator(
    input_key='invalid_input_key', shape=input_placeholder.shape
)

with self.assertRaisesRegex(
    ValueError,
    'Failed to run graph for post-training quantization calibration',
):
    quantize_model.quantize(
        self._input_saved_model_path,
        signature_keys,
        tags,
        self._output_saved_model_path,
        quantization_options,
        representative_dataset=invalid_data_gen,
    )
