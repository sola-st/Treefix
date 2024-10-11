# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
save_tags = {tag_constants.TRAINING, tag_constants.GPU}

input_placeholder = self._create_and_save_tf1_conv_model(
    self._input_saved_model_path,
    signature_key,
    save_tags,
    input_key='input',
    output_key='output',
    use_variable=True,
)

signature_keys = [signature_key]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

# Try to use a different set of tags to quantize.
tags = {tag_constants.SERVING}
data_gen = self._create_data_generator(
    input_key='input', shape=input_placeholder.shape
)
with self.assertRaisesRegex(
    RuntimeError,
    "MetaGraphDef associated with tags {'serve'} could not be found",
):
    quantize_model.quantize(
        self._input_saved_model_path,
        signature_keys,
        tags,
        self._output_saved_model_path,
        quantization_options,
        representative_dataset=data_gen,
    )
