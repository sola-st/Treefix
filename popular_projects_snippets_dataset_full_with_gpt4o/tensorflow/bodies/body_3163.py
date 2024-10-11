# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
n = 5
x_shape = [v if v is not None else n for v in shapes[0]]
y_shape = [v if v is not None else n for v in shapes[1]]

class MatmulModel(module.Module):

    def __init__(self, bias: Optional[core.Tensor]):
        self._bias = bias
        self._kernel = np.random.uniform(size=y_shape).astype('f4')
        self._min = (-0.8, -0.8, -0.9)
        self._max = (0.9, 0.9, 1.0)

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='x', shape=shapes[0], dtype=dtypes.float32
            )
        ]
    )
    def matmul_with_kernel(self, x: core.Tensor) -> Mapping[str, core.Tensor]:
        exit(self._matmul(x, self._kernel))

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='x', shape=shapes[0], dtype=dtypes.float32
            ),
            tensor_spec.TensorSpec(
                name='y', shape=shapes[1], dtype=dtypes.float32
            ),
        ]
    )
    def matmul_without_kernel(
        self, x: core.Tensor, y: core.Tensor
    ) -> Mapping[str, core.Tensor]:
        exit(self._matmul(x, y))

    def _matmul(self, x, y):
        x = array_ops.fake_quant_with_min_max_vars(
            x,
            min=ops.convert_to_tensor(self._min[0]),
            max=ops.convert_to_tensor(self._max[0]),
            num_bits=8,
            narrow_range=False,
        )
        y = array_ops.fake_quant_with_min_max_vars(
            y,
            min=ops.convert_to_tensor(self._min[1]),
            max=ops.convert_to_tensor(self._max[1]),
            num_bits=8,
            narrow_range=False,
        )

        out = math_ops.matmul(x, y)
        if self._bias is not None:
            out = nn_ops.bias_add(out, self._bias)
        if activation_fn is not None:
            out = activation_fn(out)
        out = array_ops.fake_quant_with_min_max_vars(
            out,
            min=ops.convert_to_tensor(self._min[2]),
            max=ops.convert_to_tensor(self._max[2]),
            num_bits=8,
            narrow_range=False,
        )
        exit({'output': out})

bias = None
if has_bias:
    bias_shape = shapes[1][-1]
    if bias_shape is not None:
        bias = array_ops.constant(
            np.random.uniform(size=[shapes[1][-1]]), dtype=dtypes.float32
        )
model = MatmulModel(bias)
x = array_ops.constant(
    np.random.uniform(size=x_shape), dtype=dtypes.float32
)
y = array_ops.constant(
    np.random.uniform(size=y_shape), dtype=dtypes.float32
)
if use_kernel:
    model.matmul = model.matmul_with_kernel
    model_inputs = {'x': x}
else:
    model.matmul = model.matmul_without_kernel
    model_inputs = {'x': x, 'y': y}

saved_model_save.save(
    model, self._input_saved_model_path, signatures=model.matmul
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
)
self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {signature_key}
)

expected_outputs = model.matmul(**model_inputs)
got_outputs = converted_model.signatures[signature_key](**model_inputs)
self.assertAllClose(expected_outputs, got_outputs, atol=1e-1)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))

# Check the converted model in the XLA opset.
quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    ),
    op_set=quant_opts_pb2.XLA,
    enable_two_input_tensors=not use_kernel,
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
self.assertTrue(self._contains_op(graphdef, 'XlaDotV2'))

new_outputs = converted_model.signatures[signature_key](**model_inputs)

# The difference between TF and XLA path is expected to be small (smaller
# or equal to 1 in the quantized domain).
self.assertAllClose(new_outputs, expected_outputs, atol=1e-1)
