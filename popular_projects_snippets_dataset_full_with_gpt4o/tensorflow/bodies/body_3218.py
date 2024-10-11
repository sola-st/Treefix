# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
filter_shape = (2, 3, 1024, 2)
strides = (1, 2, 2, 1)

model = self._create_depthwise_conv2d_model(
    input_shape=(1, 3, 4, 1024), filter_shape=filter_shape, strides=strides
)

saved_model_save.save(model, self._input_saved_model_path)

tags = [tag_constants.SERVING]

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.DYNAMIC_RANGE
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
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def

# Uniform Quantized op takes only the first and the second values for
# strides.
strides_to_check = (
    (strides[1], strides[2])
    if target_opset == quant_opts_pb2.UNIFORM_QUANTIZED
    else strides
)
strides_attr = attr_value_pb2.AttrValue(
    list=attr_value_pb2.AttrValue.ListValue(i=strides_to_check)
)

if enable_per_channel_quantization:
    quantized_axis_attr = attr_value_pb2.AttrValue(i=3)
    quantized_dim_size_attr = attr_value_pb2.AttrValue(
        list=attr_value_pb2.AttrValue.ListValue(
            shape=[
                tensor_shape_pb2.TensorShapeProto(
                    dim=[
                        tensor_shape_pb2.TensorShapeProto.Dim(
                            size=filter_shape[2] * filter_shape[3]
                        )
                    ]
                )
            ]
        )
    )

if target_opset == quant_opts_pb2.UNIFORM_QUANTIZED:
    self.assertTrue(
        self._contains_op(
            output_graphdef,
            'UniformQuantizedConvolutionHybrid',
            'window_strides',
            strides_attr,
        )
    )
    self.assertFalse(
        self._contains_op(output_graphdef, 'DepthwiseConv2dNative')
    )
    if enable_per_channel_quantization:
        self.assertTrue(
            self._contains_op(
                output_graphdef,
                'UniformQuantizedConvolutionHybrid',
                'rhs_quantization_axis',
                quantized_axis_attr,
            )
        )
        self.assertTrue(
            self._contains_op(
                output_graphdef,
                'Const',
                '_output_shapes',
                quantized_dim_size_attr,
            )
        )
elif target_opset == quant_opts_pb2.XLA:
    self.assertTrue(self._contains_op(output_graphdef, 'XlaConvV2'))
    self.assertFalse(
        self._contains_op(output_graphdef, 'DepthwiseConv2dNative')
    )
else:
    self.assertTrue(self._contains_quantized_function_call(output_graphdef))
    self.assertTrue(
        self._contains_op(
            output_graphdef, 'DepthwiseConv2dNative', 'strides', strides_attr
        )
    )
