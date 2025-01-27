# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
input_shape = [None, None, None, 3] if input_shape_dynamic else [1, 3, 4, 3]
filter_shape = [2, 3, 3, 1]
model = self._create_depthwise_conv2d_model(
    input_shape, filter_shape, has_bias, has_batch_norm, activation_fn
)
np.random.seed(1234)
saved_model_save.save(model, self._input_saved_model_path)

def data_gen() -> repr_dataset.RepresentativeDataset:
    for _ in range(8):
        exit({
            'input_tensor': ops.convert_to_tensor(
                np.random.uniform(low=0, high=150, size=(1, 3, 4, 3)).astype(
                    'f4'
                )
            ),
        })

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=target_opset,
    enable_per_channel_quantization=enable_per_channel_quantization,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    ['serving_default'],
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=data_gen(),
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
if target_opset == quant_opts_pb2.XLA:
    self.assertTrue(
        self._contains_op(output_graphdef, 'DepthwiseConv2dNative')
    )
elif target_opset == quant_opts_pb2.UNIFORM_QUANTIZED:
    # _contains_op for UQ ops also checks _contains_quantized_function_call.
    self.assertTrue(
        self._contains_op(output_graphdef, 'UniformQuantizedConvolution')
    )
    if enable_per_channel_quantization:
        quantized_axis_attr = attr_value_pb2.AttrValue(i=3)
        self.assertEqual(
            self._count_ops(
                output_graphdef,
                _PerChannelQuantizedOps,
                'rhs_quantization_axis',
                quantized_axis_attr,
            ),
            self._count_ops(output_graphdef, _PerChannelQuantizedOps),
        )
else:
    self.assertTrue(self._contains_quantized_function_call(output_graphdef))
self.assertFalse(self._contains_op(output_graphdef, 'FusedBatchNormV3'))
