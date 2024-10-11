# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Defines a dense layer with quantized outputs.

      Args:
        x: input to the dense layer
        num_inputs: number of input columns of x
        num_outputs: number of output columns
        quantization_range: the min/max range for quantization
        name: name of the variable scope

      Returns:
        The output of the layer.
      """
with variable_scope.variable_scope(name):
    kernel = variable_scope.get_variable(
        'kernel',
        shape=[num_inputs, num_outputs],
        dtype=dtypes.float32,
        initializer=init_ops.GlorotUniform())
    bias = variable_scope.get_variable(
        'bias',
        shape=[num_outputs],
        dtype=dtypes.float32,
        initializer=init_ops.Zeros())
    x = math_ops.matmul(x, kernel)
    x = _Quantize(x, quantization_range)
    x = nn.bias_add(x, bias)
    x = _Quantize(x, quantization_range)
exit(x)
