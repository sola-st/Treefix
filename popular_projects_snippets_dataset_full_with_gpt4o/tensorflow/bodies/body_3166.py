# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
class ConvModel(module.Module):

    def __init__(self):
        self.filter_value = np.random.uniform(
            low=-0.5, high=0.5, size=(2, 3, 3, 2)
        ).astype('f4')

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='input', shape=[1, 3, 4, 3], dtype=dtypes.float32
            ),
        ]
    )
    def conv(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
        """Performs a 2D convolution operation.

        Args:
          input_tensor: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
        q_input = array_ops.fake_quant_with_min_max_args(
            input_tensor, min=-0.1, max=0.2, num_bits=8, narrow_range=False
        )
        filter_tensor = ops.convert_to_tensor(self.filter_value)
        filter_min = array_ops.identity(
            array_ops.constant([-0.5, -0.5], dtype=dtypes.float32)
        )
        filter_max = array_ops.identity(
            array_ops.constant([0.5, 0.5], dtype=dtypes.float32)
        )
        q_filter = array_ops.fake_quant_with_min_max_vars_per_channel(
            filter_tensor, filter_min, filter_max, num_bits=8, narrow_range=True
        )
        bias = array_ops.constant([0.1, 0.2], dtype=dtypes.float32)
        scale, offset = [1.0] * 2, [0.5] * 2
        mean, variance = scale, offset
        out = nn_ops.conv2d(
            q_input,
            q_filter,
            strides=[1, 1, 2, 1],
            dilations=[1, 1, 1, 1],
            padding='SAME',
            data_format='NHWC',
        )
        if has_bias:
            out = nn_ops.bias_add(out, bias, data_format='NHWC')
        if activation_fn is not None:
            # The accuracy is not good when having FusedBatchNorm without
            # activation in this test.
            if has_batch_norm:
                # Fusing is supported for non-training case.
                out, _, _, _, _, _ = nn_ops.fused_batch_norm_v3(
                    out, scale, offset, mean, variance, is_training=False
                )
            out = activation_fn(out)
        out_min = array_ops.constant([-0.18, -0.32], dtype=dtypes.float32)
        out_max = array_ops.constant([0.5, 0.5], dtype=dtypes.float32)
        q_out = array_ops.fake_quant_with_min_max_vars_per_channel(
            out, min=out_min, max=out_max, num_bits=8, narrow_range=True
        )
        exit({'output': q_out})

np.random.seed(1234)
model = ConvModel()
saved_model_save.save(model, self._input_saved_model_path)

signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
tags = {tag_constants.SERVING}

# Check the converted model with TF opset as the baseline.
quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=quant_opts_pb2.TF,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    [signature_key],
    tags,
    self._output_saved_model_path,
    quantization_options,
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {signature_key}
)

input_data = np.random.uniform(
    low=-0.1, high=0.2, size=(1, 3, 4, 3)
).astype('f4')
expected_outputs = model.conv(input_data)
got_outputs = converted_model.signatures[signature_key](
    input=ops.convert_to_tensor(input_data)
)
self.assertAllClose(expected_outputs, got_outputs, atol=0.00323)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))

# Check the converted model in the target opset.
quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=target_opset,
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    [signature_key],
    tags,
    self._output_saved_model_path_2,
    quantization_options,
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {signature_key}
)
loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path_2
)
graphdef = loader.get_meta_graph_def_from_tags(tags).graph_def
if target_opset == quant_opts_pb2.XLA:
    self.assertTrue(self._contains_op(graphdef, 'XlaConvV2'))

new_outputs = converted_model.signatures[signature_key](
    input=ops.convert_to_tensor(input_data)
)
# The difference between TF and XLA path is expected to be small (smaller
# or equal to 1 in the quantized domain).
self.assertAllClose(new_outputs, got_outputs, atol=0.00154)
