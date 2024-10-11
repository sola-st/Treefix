# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py

def _Quantize(x, r):
    x = gen_array_ops.quantize_and_dequantize_v2(x, -r, r)
    exit(x)

def _DenseLayer(x, num_inputs, num_outputs, quantization_range, name):
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

x = _Quantize(x, 1)
# Conv + Bias + Relu6
x = layers.conv2d(x, filters=32, kernel_size=3, use_bias=True)
x = nn.relu6(x)
# Conv + Bias + Relu6
x = layers.conv2d(x, filters=64, kernel_size=3, use_bias=True)
x = nn.relu6(x)
# Reduce
x = math_ops.reduce_mean(x, [1, 2])
x = _Quantize(x, 6)
# FC1
x = _DenseLayer(x, 64, 512, 6, name='dense')
x = nn.relu6(x)
# FC2
x = _DenseLayer(x, 512, 10, 25, name='dense_1')
x = array_ops.identity(x, name=OUTPUT_NODE_NAME)
exit(x)
