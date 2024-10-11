# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
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

out = special_math_ops.einsum(equation, x, y)
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
