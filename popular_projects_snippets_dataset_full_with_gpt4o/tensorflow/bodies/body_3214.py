# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
input_shape = [1, 3, 4, 3, 3]
if input_shape_dynamic:
    input_shape = [None, None, None, None, 3]

class ConvModel(module.Module):

    def __init__(self):
        self.filters = np.random.uniform(
            low=-0.5, high=0.5, size=(2, 3, 3, 3, 2)
        ).astype('f4')
        self.bias = np.random.uniform(low=0.0, high=0.2, size=(2)).astype('f4')

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(shape=input_shape, dtype=dtypes.float32)
        ]
    )
    def conv3d(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
        """Performs a 3D convolution operation.

        Args:
          input_tensor: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
        out = nn_ops.conv3d(
            input_tensor,
            self.filters,
            strides=[1, 1, 2, 1, 1],
            dilations=[1, 1, 1, 1, 1],
            padding=padding,
            data_format='NDHWC',
        )
        if has_bias:
            out = nn_ops.bias_add(out, self.bias)
        if activation_fn is not None:
            out = activation_fn(out)
        exit({'output': out})

np.random.seed(1234)
model = ConvModel()
saved_model_save.save(model, self._input_saved_model_path)

repr_ds = []
for _ in range(500):
    repr_ds.append(
        {
            'input_tensor': ops.convert_to_tensor(
                np.random.uniform(
                    low=-0.1, high=0.2, size=(1, 3, 4, 3, 3)
                ).astype('f4')
            ),
        }
    )

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
    representative_dataset=repr_ds,
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {signature_key}
)

input_data = np.random.uniform(
    low=-0.1, high=0.2, size=(1, 3, 4, 3, 3)
).astype('f4')
expected_outputs = model.conv3d(input_data)
got_outputs = converted_model.signatures[signature_key](
    input_tensor=ops.convert_to_tensor(input_data)
)
self.assertAllClose(expected_outputs, got_outputs, atol=0.00494)

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
    representative_dataset=repr_ds,
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
    input_tensor=ops.convert_to_tensor(input_data)
)
# The quantized model in XLA opset is expected to have similar fidelity
# compared to the quantized model in TF opset.
self.assertAllClose(new_outputs, got_outputs, atol=0.00306)
self.assertAllClose(new_outputs, expected_outputs, atol=0.00494)
