# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
self._create_matmul_model(
    input_shape=(1, 1024),
    weight_shape=(1024, 3),
    saved_model_path=self._input_saved_model_path,
)

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.DYNAMIC_RANGE
    ),
    op_set=quant_opts_pb2.OpSet.UNIFORM_QUANTIZED,
)
quantization_options.min_num_elements_for_weights = num_elements

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
type_attr = attr_value_pb2.AttrValue(type=types_pb2.DT_QINT8)
if quantize:
    self.assertTrue(
        self._contains_op(output_graphdef, 'Const', 'dtype', type_attr)
    )
else:
    self.assertFalse(
        self._contains_op(output_graphdef, 'Const', 'dtype', type_attr)
    )
