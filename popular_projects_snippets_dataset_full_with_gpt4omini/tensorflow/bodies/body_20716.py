# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with multiple paths."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([2, 8, 8, 3])
    x1, x2, x3 = array_ops.split(x, num_or_size_splits=3, axis=3)
    y1 = _conv_pool(x1)
    y2 = _conv_pool(x2)
    y3 = _conv_pool(x3)
    y = array_ops.concat([y1, y2, y3], axis=3)
    y = array_ops.identity(y)
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x])
    output = (y, g)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'split')
for suffix in [''] + ['_%i' % i for i in range(1, 6)]:
    self._assert_output_f16(mode, node_map, 'Conv2D' + suffix)
    self._assert_output_f16(mode, node_map, 'Relu' + suffix)
    self._assert_output_f16(mode, node_map, 'MaxPool' + suffix)
self._assert_output_f16(mode, node_map, 'concat')
atol = 1e-2 if test.is_built_with_rocm() else 1e-3
self.assertAllClose(output_val_ref, output_val, atol=atol, rtol=1e-3)
