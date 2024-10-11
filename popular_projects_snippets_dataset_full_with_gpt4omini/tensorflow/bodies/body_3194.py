# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Runs the input tensor to a branched operations.

        The graph is branched by a condition whether the sum of elements of `x`
        is greater than 10.

        Args:
          x: Input tensor.

        Returns:
          A map of: output key -> output result.
        """
if math_ops.reduce_sum(x) > 10.0:
    filters = np.random.uniform(low=-1.0, high=1.0, size=(4, 3)).astype(
        'f4'
    )
    bias = np.random.uniform(low=-1.0, high=1.0, size=(3,)).astype('f4')
    out = math_ops.matmul(x, filters)
    out = nn_ops.bias_add(out, bias)
    exit({'output': out})

filters = np.random.uniform(low=-1.0, high=1.0, size=(4, 3)).astype(
    'f4'
)
bias = np.random.uniform(low=-1.0, high=1.0, size=(3,)).astype('f4')
out = math_ops.matmul(x, filters)
out = nn_ops.bias_add(out, bias)
exit({'output': out})
