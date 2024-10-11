# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test grad ops with depthwise convolution2d graph."""
self._maybe_skip(mode)
cudnn_version_str = sysconfig_lib.get_build_info().get(
    'cudnn_version', '0.0')
cudnn_version = tuple([int(x) for x in cudnn_version_str.split('.')])
if cudnn_version < (8,):
    # Depthwise conv2d ops are only enabled in auto_mixed_precision as of
    # cuDNN v8.
    self.skipTest('cuDNN version >= 8 required')
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 1])
    f = _weight([3, 3, 1, 4])
    y = _depthwise_conv2d(x, f)
    y = array_ops.identity(y)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x, f])
    output = (y, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
self._assert_output_f16(mode, node_map, 'depthwise')
self._assert_output_f16(
    mode, node_map,
    'gradients/depthwise_grad/DepthwiseConv2dNativeBackpropInput')
self._assert_output_f16(
    mode, node_map,
    'gradients/depthwise_grad/DepthwiseConv2dNativeBackpropFilter')

output_val_ref, output_val, cost_graph = self._run(mode, output)
tol = 2e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
