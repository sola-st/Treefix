# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
# Use a different set of tags other than {"serve"}.
tags = {tag_constants.TRAINING, tag_constants.GPU}

# Non-default tags are usually used when saving multiple metagraphs in TF1.
input_placeholder = self._create_and_save_tf1_conv_model(
    self._input_saved_model_path,
    signature_key,
    tags,
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

data_gen = self._create_data_generator(
    input_key='input', shape=input_placeholder.shape
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=data_gen,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), signature_keys
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
