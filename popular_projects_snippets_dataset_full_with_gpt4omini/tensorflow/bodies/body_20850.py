# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
"""Test Conv2D+BiasAdd+Relu fusion."""
if not test_util.is_gpu_available():
    self.skipTest('No GPU available')

N, H, W, C = (5, 3, 3, 8)  # pylint: disable=invalid-name
# The runtime fusion requires the output dims to be 32-bit aligned.
self.assertEqual(C % 2, 0)

act_fns = [nn.relu]
act_names = [b'Relu']

if test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    act_fns += [nn.elu, nn.relu6, nn.leaky_relu]
    act_names += [b'Elu', b'Relu6', b'LeakyRelu']

for precision in ('float16', 'float32'):
    for act_fn, act_name in zip(act_fns, act_names):
        use_fp16 = precision == 'float16'
        # The runtime fusion (when the activation is not relu) only supports
        # fp16 at this moment.
        if not use_fp16 and act_name != b'Relu':
            continue

        ops.reset_default_graph()
        x_shape = [N, C, H, W]
        x_format, b_format = ('NCHW', 'NC..')
        if use_fp16:
            x_shape = [N, H, W, C]
            x_format, b_format = ('NHWC', 'N..C')

        x = _input(x_shape)
        w = _weight([2, 2, C, C])
        b = _bias([C])

        if use_fp16:
            x = math_ops.cast(x, dtypes.float16)
            w = math_ops.cast(w, dtypes.float16)
            b = math_ops.cast(b, dtypes.float16)

        y = nn_ops.conv2d(
            x, w, strides=(1, 1), padding='SAME', data_format=x_format)
        z = nn.bias_add(y, b, data_format=b_format)
        out = act_fn(z)
        out = array_ops.identity(out)

        epilog_ops = [b'BiasAdd', act_name]
        fused_op = ['_FusedConv2D']
        graph = self._VerifyValues(out, use_fp16, fused_op, epilog_ops)
