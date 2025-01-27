# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Test graph with multiple paths."""
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    x = _input([8, 8])
    y1 = _matmul_act(x)
    y2 = _matmul_act(x)
    y = y1 + y2 + x
    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.01)
    g = optimizer.compute_gradients(y, [x])
    output = (g, y)

output_val_ref, output_val, cost_graph = self._run(mode, output)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'MatMul')
self._assert_output_f16(mode, node_map, 'Relu')
self._assert_output_f16(mode, node_map, 'MatMul_1')
self._assert_output_f16(mode, node_map, 'Relu_1')
if mode == 'mkl':
    tol = 2e-2
elif test.is_built_with_rocm():
    # Bump up the tolerance for the ROCm platform
    # The default tolerance (1e-3) results in a tiny fraction (<1%) of
    # miscompares on ROCm platform, and hence the tolerance bump
    tol = 1e-2
else:
    tol = 1e-3
self.assertAllClose(output_val_ref, output_val, atol=tol, rtol=tol)
