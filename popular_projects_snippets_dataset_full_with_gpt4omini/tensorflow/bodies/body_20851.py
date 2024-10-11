# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
"""Test two Conv2D patterns and only the second is fusable."""
if not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest('No GPU with compute compatibility >= 8.0 available')

N, H, W, C = (5, 3, 3, 8)  # pylint: disable=invalid-name

ops.reset_default_graph()
x_shape = [N, C, H, W]
x_format, b_format = ('NCHW', 'NC..')

x = _input(x_shape)
w = _weight([2, 2, C, C])
b = _bias([C])

y = nn_ops.conv2d(
    x, w, strides=(1, 1), padding='SAME', data_format=x_format)
y = nn.bias_add(y, b, data_format=b_format)
y = nn.leaky_relu(y)
y = nn_ops.conv2d(
    y, w, strides=(1, 1), padding='SAME', data_format=x_format)
y = nn.bias_add(y, b, data_format=b_format)
y = nn.relu(y)
out = array_ops.identity(y)

# The first Conv-BiasAdd-LeakyRelu is not fusable because cuDNN requires
# fp16 for this pattern. The second Conv-BiasAdd-Relu is fusable.
epilog_ops = [b'BiasAdd', b'Relu']
fused_op = ['_FusedConv2D']
self._VerifyValues(out, False, fused_op, epilog_ops)
