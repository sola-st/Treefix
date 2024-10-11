# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test grad ops with convolution3d graph."""
self._maybe_skip(mode)
if mode == 'cuda':
    # TODO(reedwm): enable these tests when cuDNN is upgraded to >= 7.6.2.
    self.skipTest('Test case should be skipped when cuDNN < 7.6.2')
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 8, 1])
    f = _weight([3, 3, 3, 1, 6])
    y = _conv3d(x, f)
    y = array_ops.identity(y)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x, f])
    output = (y, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
self._assert_output_f16(mode, node_map, 'Conv3D')
self._assert_output_f16(mode, node_map,
                        'gradients/Conv3D_grad/Conv3DBackpropInputV2')
self._assert_output_f16(mode, node_map,
                        'gradients/Conv3D_grad/Conv3DBackpropFilterV2')

output_val_ref, output_val, cost_graph = self._run(mode, output)
tol = 5e-2 if mode == 'mkl' else 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
