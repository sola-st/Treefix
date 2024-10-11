# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test dropout precision of convolution batch norm graph."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 1])
    y = _conv_bn(x)
    y = nn.dropout(y, rate=0.5)
    y = math_ops.add(y, 1, name='addition')
    y = _conv_bn(y)
    y = array_ops.identity(y)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x])
    output = (y, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)
self._assert_output_f16(mode, node_map, 'Conv2D')
self._assert_output_f16(mode, node_map, 'FusedBatchNormV3')
# We do not assert dropout's dtype because we do not want to rely on the
# node names of dropout's internal implementation.
self._assert_output_f16(mode, node_map, 'addition')
self._assert_output_f16(mode, node_map, 'Conv2D_1')

output_val_ref, output_val, cost_graph = self._run(mode, output)
# Bump up the tolerance for the ROCm platform
# The default tolerance (1e-3) results in a tiny fraction (<1%) of
# miscompares on ROCm platform, and hence the tolerance bump
tol = 2e-3 if test.is_built_with_rocm else 1e-3
tol = 5e-2 if mode == 'mkl' else tol
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
